#groupby - agrrupando valores

from itertools import groupby

alunos = [
    {'nome': 'Juliana', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Vitor', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Julia', 'nota': 'A'},
    {'nome': 'Joaquim', 'nota': 'B'},
    {'nome': 'Joaquina', 'nota': 'C'},
    {'nome': 'Tiago', 'nota': 'D'}
]

def ordena(aluno):
    return aluno['nota']


# alunos = ['a','a','a','b','c','d']

alunos_agrupados = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno['nome'])