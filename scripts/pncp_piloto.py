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
DIRECT = re.compile(r"\bcorrim[aã]o(?:s)?\b|\bguarda[ -]?corpo(?:s)?\b|\ba[cç]o\s+inox(?:id[aá]vel)?\b|\binox\b|\bABNT\b|\bNBR\s*[-:]?\s*(?:9050|14718)\b|\bgradil\b|\bserralheria\b|\bestrutura[s]? met[aá]lica[s]?\b|\bpassarela\b|\bacessibilidade\b", re.I)
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uf", default="SP")
    parser.add_argument("--dias", type=int, default=30, help="Prazo futuro de propostas")
    parser.add_argument("--paginas", type=int, default=1, help="Máximo de páginas (10 registros cada)")
    parser.add_argument("--saida", default="resultado-pncp.json")
    args = parser.parse_args()
    if not 1 <= args.paginas <= 10 or not 1 <= args.dias <= 90:
        parser.error("Use paginas de 1 a 10 e dias de 1 a 90")
    deadline = (date.today() + timedelta(days=args.dias)).strftime("%Y%m%d")
    found = {}
    total_read = 0
    errors = []
    for page in range(1, args.paginas + 1):
        try:
            payload = fetch({"dataFinal": deadline, "uf": args.uf, "pagina": page, "tamanhoPagina": 10})
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append({"pagina": page, "tipo": type(exc).__name__, "mensagem": str(exc)})
            break
        items = payload.get("data") or []
        total_read += len(items)
        for item in items:
            obj = item.get("objetoCompra") or ""
            classification = "direta" if DIRECT.search(obj) else "obra_para_prospeccao" if INDIRECT.search(obj) else None
            if not classification:
                continue
            key = item.get("numeroControlePNCP")
            if not key:
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
    result = {"fonte": BASE, "uf": args.uf, "consulta_em": date.today().isoformat(), "registros_lidos": total_read, "candidatos": list(found.values()), "erros": errors, "status": "falha" if errors and total_read == 0 else "parcial" if errors else "ok"}
    with open(args.saida, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    print(f"Registros lidos: {total_read}; candidatos preliminares: {len(found)}; arquivo: {args.saida}")
    return 1 if errors else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Falha na consulta PNCP: {exc}", file=sys.stderr)
        sys.exit(1)
