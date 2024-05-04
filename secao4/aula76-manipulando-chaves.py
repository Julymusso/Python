'''
Manipulando chaves e valores
'''

pessoa = {}

chave = 'nome'

pessoa [chave] = 'Juliana'
pessoa ['sobrenome'] = 'Silva'

print(pessoa[chave])

pessoa[chave] = 'João'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não tem sobrenome')
else:
    print(pessoa['sobrenome'])



















print(pessoa)
