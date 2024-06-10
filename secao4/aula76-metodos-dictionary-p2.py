'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Juliana',
    'sobrenome': 'Musso',
    'idade': 33
}

# del pessoa['nome']
# print(pessoa.get('nome','Não existe'))

# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

# last_word = pessoa.popitem()
# print(last_word)
# print(pessoa)

pessoa.update({
    'nome': 'Janaina',
    'idade': 34})

print (pessoa)

pessoa.update(nome='Jose', idade=50)
print(pessoa)

tupla = ('nome', 'Juliana'), ('idade', 33)
pessoa.update(tupla)
print(pessoa)