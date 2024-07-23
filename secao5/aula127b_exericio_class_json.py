# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json
from aula127a_exericio_class_json import FILE_PATH, Pessoa

with open(FILE_PATH,'r') as arquivo:
    pessoas = json.load(arquivo)

print (pessoas)

for p in pessoas:
    p1 = Pessoa(**p)
    p2 = Pessoa(**p)
    p3 = Pessoa(**p)
    p4 = Pessoa(**p)
    p5 = Pessoa(**p)
    p6 = Pessoa(**p)