"""Dados de planejamento: somente arquivos locais, sem dependências externas."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import secrets

ROOT = Path(__file__).resolve().parents[1]


def resultado(total):
    return 'sucesso' if total >= 10 else 'parcial' if total >= 7 else 'falha'


def validar(plano):
    if not isinstance(plano, dict):
        raise ValueError('O plano deve ser um objeto JSON.')
    if plano.get('tipo') == 'sorteio':
        ident = plano.get('id', '')
        if not ident or len(ident) > 80 or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-_' for c in ident):
            raise ValueError('id inválido para sorteio.')
        opcoes = plano.get('opcoes')
        faces = plano.get('faces', 6)
        if not isinstance(opcoes, list) or len(opcoes) < 2 or any(not isinstance(x, str) or not x.strip() for x in opcoes):
            raise ValueError('Defina ao menos duas opções antes do sorteio.')
        if len(set(opcoes)) != len(opcoes):
            raise ValueError('Opções repetidas alterariam as probabilidades.')
        if type(faces) is not int or not 2 <= faces <= 1000 or faces % len(opcoes):
            raise ValueError('faces deve ser múltiplo da quantidade de opções, entre 2 e 1000.')
        if not plano.get('objetivo'):
            raise ValueError('Defina o objetivo do sorteio.')
        return plano
    for campo in ('id', 'cena', 'objetivo', 'obstaculo', 'categoria', 'sucesso', 'parcial', 'falha'):
        if not isinstance(plano.get(campo), str) or not plano[campo].strip():
            raise ValueError(f'Preencha {campo} antes de rolar.')
    ident = plano['id']
    if len(ident) > 80 or any(c not in 'abcdefghijklmnopqrstuvwxyz0123456789-_' for c in ident):
        raise ValueError('id: use até 80 letras minúsculas ASCII, números, - ou _.')
    modificador = plano.get('modificador', 0)
    if type(modificador) is not int or not -3 <= modificador <= 3:
        raise ValueError('modificador deve ser inteiro entre -3 e 3.')
    if modificador and not plano.get('justificativa_modificador'):
        raise ValueError('Justifique o modificador antes de rolar.')
    if plano.get('pista_essencial') and not plano.get('rota_alternativa'):
        raise ValueError('Pista essencial exige rota_alternativa para a falha.')
    return plano


def executar(plano, randbelow=secrets.randbelow):
    validar(plano)
    if plano.get('tipo') == 'sorteio':
        faces = plano.get('faces', 6)
        face = randbelow(faces) + 1
        indice = (face - 1) // (faces // len(plano['opcoes']))
        return {'data_utc': datetime.now(timezone.utc).isoformat(), 'regra': 'sorteio-equiprovavel-v1',
                'plano': plano, 'dados': [face], 'resultado': plano['opcoes'][indice],
                'probabilidade_por_opcao': f"1/{len(plano['opcoes'])}"}
    dados = [randbelow(6) + 1 for _ in range(2)]
    total = sum(dados) + plano.get('modificador', 0)
    grau = resultado(total)
    return {'data_utc': datetime.now(timezone.utc).isoformat(), 'regra': '2d6-v1',
            'plano': plano, 'dados': dados, 'total': total,
            'resultado': grau, 'consequencia': plano[grau]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plano', type=Path, help='JSON com obstáculo e três consequências previamente definidos')
    parser.add_argument('--validar', action='store_true', help='Valida sem sortear nem registrar')
    parser.add_argument('--simular', action='store_true', help='Sorteio de teste, sem valor narrativo e sem registro')
    parser.add_argument('--historico', type=Path, default=ROOT / 'docs/planejamento/rolagens')
    args = parser.parse_args()
    try:
        plano = validar(json.loads(args.plano.read_text(encoding='utf-8-sig')))
        if args.validar:
            print('Plano válido. Nenhuma rolagem realizada.')
            return
        if args.simular:
            registro = executar(plano)
            registro['simulacao'] = True
        else:
            args.historico.mkdir(parents=True, exist_ok=True)
            destino = args.historico / (plano['id'] + '.json')
            # Criação exclusiva impede repetir silenciosamente o mesmo obstáculo.
            with destino.open('x', encoding='utf-8') as arquivo:
                registro = executar(plano)
                json.dump(registro, arquivo, ensure_ascii=False, indent=2)
                arquivo.write('\n')
            print(f'Registro: {destino}')
        print(json.dumps(registro, ensure_ascii=False, indent=2))
    except FileExistsError:
        parser.exit(2, 'Este id já foi rolado. Consulte o registro; não repita para obter outro resultado.\n')
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Erro: {exc}\n')


if __name__ == '__main__':
    main()
