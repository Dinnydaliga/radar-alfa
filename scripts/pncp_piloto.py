#!/usr/bin/env python3
"""Piloto PNCP: consulta pública, filtro inicial e saída local JSON (sem envio)."""
import argparse
import time
import socket
import urllib.error
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta

BASE = "https://pncp.gov.br/api/consulta/v1/contratacoes/proposta"
DIRECT = re.compile(r"corrim[aã]o|guarda[ -]?corpo|gradil|serralheria|estrutura[s]? met[aá]lica[s]?|passarela|acessibilidade", re.I)
INDIRECT = re.compile(r"constru[cç][aã]o|reforma|amplia[cç][aã]o|obra[s]?|engenharia|hospital|escola|pr[eé]dio", re.I)


def fetch(params, timeout=18, attempts=2):
    url = BASE + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "radar-alfa-piloto/0.2"})
    for attempt in range(1, attempts + 1):
        start = time.monotonic()
        try:
            print(f"PNCP: pagina {params['pagina']}, tentativa {attempt}/{attempts}, timeout {timeout}s", flush=True)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = json.load(response)
            if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
                raise ValueError("Resposta inesperada: campo 'data' ausente ou nao e lista")
            print(f"PNCP: resposta recebida em {time.monotonic()-start:.1f}s", flush=True)
            return payload
        except (TimeoutError, socket.timeout, urllib.error.URLError, urllib.error.HTTPError) as exc:
            print(f"PNCP: falha apos {time.monotonic()-start:.1f}s: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == attempts:
                raise
            time.sleep(2 * attempt)


def classify(item):
    obj = item.get("objetoCompra") or ""
    if DIRECT.search(obj):
        return "direta"
    if INDIRECT.search(obj):
        return "obra_para_prospeccao"
    return "descartada"


def summarize(result, destination):
    """Resumo legível no GitHub Actions; não depende do artefato."""
    from pathlib import Path
    from datetime import datetime, timezone
    counts = result["contagens"]
    lines = [
        "# Radar Alfa — consulta PNCP",
        f"- Situação: **{result['status']}**",
        f"- UF: {result['uf']} | Consulta: {result['consulta_em']} | Prazo final pesquisado: {result['data_final_parametro']}",
        "- Cobertura: **parcial / piloto limitado**; não representa todas as licitações de SP.",
        f"- Registros lidos: **{result['registros_lidos']}**; únicos: **{result['registros_unicos']}**; duplicados: **{result['duplicados']}**",
        f"- Diretas: **{counts['direta']}**; indiretas: **{counts['obra_para_prospeccao']}**; descartadas: **{counts['descartada']}**",
        f"- Páginas consultadas: **{result['paginas_consultadas']}**; erros: **{len(result['erros'])}**",
        "",
        "## Oportunidades preliminares",
        "| Tipo | Órgão | Município | Objeto | Valor global | Prazo | Link fornecido pela origem |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    def cell(value):
        return str(value if value is not None and value != "" else "não informado").replace("|", "&#124;").replace("\n", " ")[:250]
    for c in result["candidatos"]:
        url = c.get("link")
        link = f"[Abrir]({url})" if isinstance(url, str) and url.startswith(("https://", "http://")) else "não informado"
        lines.append("| " + " | ".join([
            cell(c["classificacao_preliminar"]), cell(c["orgao"]), cell(c["municipio"]),
            cell(c["objeto"]), cell(c["valor_global_estimado"]), cell(c["data_fim_propostas"]), link,
        ]) + " |")
    if not result["candidatos"]:
        lines.append("| Nenhuma oportunidade preliminar | — | — | — | — | — | — |")
    if result["erros"]:
        lines.extend(["", "## Erros"])
        for err in result["erros"]:
            lines.append(f"- Página {err['pagina']}: {cell(err['tipo'])} — {cell(err['mensagem'])}")
    lines.extend(["", "Classificação automática preliminar. Conferir edital, prazo e valor do escopo Alfa antes de prospectar. O link de origem não é necessariamente a página oficial PNCP."])
    Path(destination).write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_console_report(result):
    """Relatório em texto puro, legível nos logs da etapa Consultar PNCP."""
    counts = result["contagens"]
    print("\\n===== RADAR ALFA PNCP — RESULTADO =====")
    print(f"Status: {result['status']} | UF: {result['uf']} | Data: {result['consulta_em']}")
    print(f"Registros lidos: {result['registros_lidos']} | Únicos: {result['registros_unicos']} | Duplicados: {result['duplicados']}")
    print(f"Diretas: {counts['direta']} | Indiretas: {counts['obra_para_prospeccao']} | Descartadas: {counts['descartada']}")
    print(f"Páginas consultadas: {result['paginas_consultadas']} | Erros: {len(result['erros'])}")
    print("Cobertura: piloto limitado; não representa todo o Estado de SP.")
    for index, item in enumerate(result["candidatos"], 1):
        print(f"\\nOPORTUNIDADE {index} — {item['classificacao_preliminar']}")
        for label, key in [
            ("PNCP ID", "numeroControlePNCP"), ("Órgão", "orgao"),
            ("Município", "municipio"), ("Objeto", "objeto"),
            ("Valor global", "valor_global_estimado"), ("Prazo", "data_fim_propostas"),
            ("Link de origem (não necessariamente PNCP)", "link")
        ]:
            print(f"{label}: {item.get(key) if item.get(key) is not None else 'não informado'}")
    if not result["candidatos"]:
        print("Nenhuma oportunidade preliminar encontrada nos registros consultados.")
    for err in result["erros"]:
        print(f"ERRO página {err['pagina']}: {err['tipo']} — {err['mensagem']}")
    print("Resultados preliminares; validar edital e valor do escopo Alfa.")
    print("===== FIM DO RELATÓRIO =====\\n", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uf", default="SP")
    parser.add_argument("--dias", type=int, default=30, help="Prazo futuro de propostas")
    parser.add_argument("--paginas", type=int, default=1, help="Máximo de páginas (10 registros cada)")
    parser.add_argument("--saida", default="resultado-pncp.json")
    parser.add_argument("--resumo", default=None, help="Arquivo Markdown para GitHub Actions")
    args = parser.parse_args()
    if not 1 <= args.paginas <= 10 or not 1 <= args.dias <= 90:
        parser.error("Use paginas de 1 a 10 e dias de 1 a 90")
    deadline = (date.today() + timedelta(days=args.dias)).strftime("%Y%m%d")
    found = {}
    total_read = 0
    errors = []
    unique = set()
    counts = {"direta": 0, "obra_para_prospeccao": 0, "descartada": 0}
    duplicates = 0
    pages_read = 0
    for page in range(1, args.paginas + 1):
        try:
            payload = fetch({"dataFinal": deadline, "uf": args.uf, "pagina": page, "tamanhoPagina": 10})
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append({"pagina": page, "tipo": type(exc).__name__, "mensagem": str(exc)})
            break
        items = payload.get("data") or []
        pages_read += 1
        total_read += len(items)
        for item in items:
            obj = item.get("objetoCompra") or ""
            key = item.get("numeroControlePNCP")
            if key and key in unique:
                duplicates += 1
                continue
            if key:
                unique.add(key)
            classification = classify(item)
            counts[classification] += 1
            if classification == "descartada" or not key:
                continue
            found[key] = {
                "numeroControlePNCP": key,
                "classificacao_preliminar": classification,
                "objeto": obj,
                "orgao": (item.get("orgaoEntidade") or {}).get("razaoSocial"),
                "municipio": (item.get("unidadeOrgao") or {}).get("municipioNome"),
                "valor_global_estimado": item.get("valorTotalEstimado"),
                "valor_escopo_alfa": "a verificar",
                "data_fim_propostas": item.get("dataEncerramentoProposta"),
                "link": item.get("linkSistemaOrigem"),
                "observacao": "Requer leitura do edital e validação técnica/comercial."
            }
        if not items or page >= payload.get("totalPaginas", page):
            break
    result = {"fonte": BASE, "uf": args.uf, "consulta_em": date.today().isoformat(), "data_final_parametro": deadline, "registros_lidos": total_read, "registros_unicos": total_read - duplicates, "duplicados": duplicates, "paginas_consultadas": pages_read, "contagens": counts, "candidatos": list(found.values()), "erros": errors, "status": "falha" if errors and total_read == 0 else "parcial" if errors else "ok"}
    with open(args.saida, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    if args.resumo:
        summarize(result, args.resumo)
    print_console_report(result)
    print(f"Registros lidos: {total_read}; candidatos preliminares: {len(found)}; arquivo: {args.saida}")
    return 1 if errors else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Falha na consulta PNCP: {exc}", file=sys.stderr)
        sys.exit(1)
