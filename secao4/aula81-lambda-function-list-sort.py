# Função lambda em Python
# A função lambda é uma função como qualquer outra em Python. 
# Porém, são funções anônimas que contém apenas uma linha.
# Ou seja, tudo deve ser contido dentro de uma única expressão.

lista = [
 {'nome': 'Juliana', 'sobrenome': 'Musso'},
 {'nome': 'Rafael', 'sobrenome': 'Nascimento'},
 {'nome': 'Mariana', 'sobrenome': 'Silva'},
 {'nome': 'João', 'sobrenome': 'Vitorino'},
 {'nome': 'Cristina', 'sobrenome': 'Santos'},
 ]

# def ordena(item):
#     return item['nome']

#lista.sort(key=ordena)

#lista.sort(key=lambda item: item['nome'])

l1 = sorted(lista, key=lambda item: item['nome'])

print (lista)

#lista = [4, 32, 1, 34, 5, 6, 6, 21]
#lista.sort() #[1, 4, 5, 6, 6, 21, 32, 34]
#sorted(lista) #[1, 4, 5, 6, 6, 21, 32, 34]
#print (lista)