"""
Listas em Pyhton
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
list()
"""
#        +01234
#        -54321

string = 'ABCDE'  # 5 caracteres (len)

lista = ['123', True, 'Juliana Musso', '1.2', ['carro', 'bicicleta']]
lista[2] = 'Maria'
lista.append('Append')
nome = lista.pop() # remove o último elemento da lista e retorna o valor
del lista [-1] # remove o último elemento da lista
lista.clear() # remove todos os elementos da lista
lista.insert(0, 5)

#print(bool([])) # false
print(lista, type(lista))
print(lista[2], type(lista[2]))


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)

