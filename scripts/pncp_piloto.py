#!/usr/bin/env python3
"""Piloto PNCP: consulta pública, filtro inicial e saída local JSON (sem envio)."""
import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import date, timedelta

BASE = "https://pncp.gov.br/api/consulta/v1/contratacoes/proposta"
DIRECT = re.compile(r"corrim[aã]o|guarda[ -]?corpo|gradil|serralheria|estrutura[s]? met[aá]lica[s]?|passarela|acessibilidade", re.I)
INDIRECT = re.compile(r"constru[cç][aã]o|reforma|amplia[cç][aã]o|obra[s]?|engenharia|hospital|escola|pr[eé]dio", re.I)


def fetch(params, timeout=25):
    url = BASE + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "radar-alfa-piloto/0.1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uf", default="SP")
    parser.add_argument("--dias", type=int, default=30, help="Prazo futuro de propostas")
    parser.add_argument("--paginas", type=int, default=2, help="Máximo de páginas (10 registros cada)")
    parser.add_argument("--saida", default="resultado-pncp.json")
    args = parser.parse_args()
    if not 1 <= args.paginas <= 10 or not 1 <= args.dias <= 90:
        parser.error("Use paginas de 1 a 10 e dias de 1 a 90")
    deadline = (date.today() + timedelta(days=args.dias)).strftime("%Y%m%d")
    found = {}
    total_read = 0
    for page in range(1, args.paginas + 1):
        payload = fetch({"dataFinal": deadline, "uf": args.uf, "pagina": page, "tamanhoPagina": 10})
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
                "link": item.get("linkSistemaOrigem") or f"https://pncp.gov.br/app/editais/{key.replace('-', '/')}",
                "observacao": "Requer leitura do edital e validação técnica/comercial."
            }
        if not items or page >= payload.get("totalPaginas", page):
            break
    result = {"fonte": BASE, "uf": args.uf, "consulta_em": date.today().isoformat(), "registros_lidos": total_read, "candidatos": list(found.values())}
    with open(args.saida, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    print(f"Registros lidos: {total_read}; candidatos preliminares: {len(found)}; arquivo: {args.saida}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Falha na consulta PNCP: {exc}", file=sys.stderr)
        sys.exit(1)
