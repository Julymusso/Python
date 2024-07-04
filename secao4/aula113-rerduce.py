﻿# reduce - faz a reduçao de um iteravel em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def func_reduce(acumulador, produto):
    print(acumulador)
    return acumulador + produto['preco']

total = reduce(
    func_reduce, 
    produtos, 
    0 #valor inicial
)

# total = 0
# for p in produtos:
#     total += p['preco']
#printar apenas 2 casa decimais

print(f'valor: {total:.2f}')