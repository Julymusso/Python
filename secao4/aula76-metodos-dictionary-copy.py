'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy) - tudo que for imutaveis ele copia, o que for mutavel ele só faz apontamento
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
import copy

pessoa = {
    'nome': 'Juliana',
    'sobrenome': 'Musso',
    'idade': 33
}

pessoa.setdefault('idade',0)
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))


d1 = {
    'a': 1,
    'b': 2,
    'l1': [0, 1, 2]
}

d2 = d1.copy()

d2['a'] = 1000
d2['l1'][1]=99

print(d1)
print(d2)

d2 = copy.deepcopy(d1)

d2['a'] = 2000
d2['l1'][1]=999

print(d1)
print(d2)