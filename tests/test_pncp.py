import importlib.util
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pncp", ROOT / "scripts" / "pncp_piloto.py")
pncp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pncp)


class RadarTests(unittest.TestCase):
    def test_classification(self):
        self.assertEqual(pncp.classify({"objetoCompra": "Peças em inox"}), "direta")
        self.assertEqual(pncp.classify({"objetoCompra": "Adequação NBR 9050"}), "direta")
        self.assertEqual(pncp.classify({"objetoCompra": "Instalação de corrimão"}), "direta")
        self.assertEqual(pncp.classify({"objetoCompra": "Reforma de escola"}), "obra_para_prospeccao")
        self.assertEqual(pncp.classify({"objetoCompra": "Compra de papel"}), "descartada")

    def run_case(self, data, error=None):
        with tempfile.TemporaryDirectory() as tmp:
            output = pathlib.Path(tmp) / "result.json"
            summary = pathlib.Path(tmp) / "summary.md"
            def fake_fetch(*args, **kwargs):
                if error:
                    raise error
                return {"data": data, "totalPaginas": 1}
            with patch.object(pncp, "fetch", side_effect=fake_fetch), patch.object(
                sys, "argv", ["pncp", "--uf", "SP", "--saida", str(output), "--resumo", str(summary)]
            ):
                code = pncp.main()
            return code, json.loads(output.read_text(encoding="utf-8")), summary.read_text(encoding="utf-8")

    def test_duplicates_missing_fields_and_summary(self):
        items = [
            {"numeroControlePNCP": "A", "objetoCompra": "Corrimão"},
            {"numeroControlePNCP": "A", "objetoCompra": "Corrimão"},
            {"numeroControlePNCP": "B", "objetoCompra": "Reforma"},
            {"numeroControlePNCP": "C", "objetoCompra": "Papel"},
        ]
        code, result, summary = self.run_case(items)
        self.assertEqual(code, 0)
        self.assertEqual(result["duplicados"], 1)
        self.assertEqual(result["contagens"], {"direta": 1, "obra_para_prospeccao": 1, "descartada": 1})
        self.assertIn("não informado", summary)

    def test_zero_results(self):
        code, result, summary = self.run_case([])
        self.assertEqual(code, 0)
        self.assertEqual(result["registros_lidos"], 0)
        self.assertEqual(result["status"], "ok")

    def test_failure_is_not_zero_results(self):
        code, result, summary = self.run_case([], TimeoutError("tempo esgotado"))
        self.assertEqual(code, 1)
        self.assertEqual(result["status"], "falha")
        self.assertEqual(len(result["erros"]), 1)
        self.assertIn("falha", summary)


if __name__ == "__main__":
    unittest.main()
