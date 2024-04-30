"""
Exercício 
Exiba os índices da lista
"""

""" lista = ['Maria', 'Helena', 'Luiz']
i = 0
for nome in lista:
    print(nome, i)
    i += 1 """

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])
