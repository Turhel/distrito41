import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/rolar_dados.py'
spec = importlib.util.spec_from_file_location('dados', SCRIPT)
dados = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dados)


class DadosTests(unittest.TestCase):
    def setUp(self):
        self.plano = json.loads((ROOT / 'docs/ferramentas/exemplo-obstaculo.json').read_text(encoding='utf-8'))

    def test_limites(self):
        for n, esperado in [(2, 'falha'), (6, 'falha'), (7, 'parcial'), (9, 'parcial'), (10, 'sucesso'), (12, 'sucesso')]:
            self.assertEqual(dados.resultado(n), esperado)
        resultado = dados.executar(self.plano, lambda _: 5)
        self.assertEqual(resultado['dados'], [6, 6])
        self.assertEqual(resultado['consequencia'], self.plano['sucesso'])

    def test_pista_nao_pode_bloquear(self):
        self.plano.pop('rota_alternativa')
        with self.assertRaises(ValueError):
            dados.validar(self.plano)

    def test_sorteio_equiprovavel(self):
        plano = {'tipo': 'sorteio', 'id': 'teste-sorteio', 'objetivo': 'teste', 'faces': 6, 'opcoes': ['a', 'b', 'c']}
        resultados = [dados.executar(plano, lambda _, n=n: n)['resultado'] for n in range(6)]
        self.assertEqual(resultados, ['a', 'a', 'b', 'b', 'c', 'c'])
        plano['faces'] = 5
        with self.assertRaises(ValueError):
            dados.validar(plano)

    def test_registro_e_repeticao(self):
        with tempfile.TemporaryDirectory() as pasta:
            p = Path(pasta) / 'plano.json'
            p.write_text(json.dumps(self.plano), encoding='utf-8')
            history = Path(pasta) / 'historico'
            cmd = [sys.executable, str(SCRIPT), str(p), '--historico', str(history)]
            self.assertEqual(subprocess.run(cmd + ['--validar'], capture_output=True).returncode, 0)
            self.assertFalse(history.exists())
            self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
            arquivo = history / (self.plano['id'] + '.json')
            anterior = arquivo.read_bytes()
            self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)
            self.assertEqual(arquivo.read_bytes(), anterior)


if __name__ == '__main__':
    unittest.main()
