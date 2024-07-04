#Combinations, Permutations e Product - Itertools
#Combinação - Ordem não importa - iterável + tamanho do grupo
#Permutação - Ordem importa
#Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Maria',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]

print(*list(combinations(pessoas,2)),sep='\n')
print('\n')
print(*list(permutations(pessoas,2)),sep='\n')
print('\n')
print(*list(product(*camisetas)),sep='\n')
