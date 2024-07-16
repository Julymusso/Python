import json

pessoa = {
    'nome': 'Juliana',
    'sobrenome': 'Musso',
    'idade': 33,
    'enderecos': [
        {'rua': 'R. dos Bobos', 'numero': 123},
        {'rua': 'Av. dos Bobos', 'numero': 321}
    ],
    'altura': 1.65,
    'numeros_prerferidos': (1, 2, 3, 4, 5),
    'dev': True,
    'nada': None
}

with open('aula117.json', 'w+') as arquivo:
    json.dump(pessoa,arquivo,ensure_ascii=False,indent=4)

with open('aula117.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)