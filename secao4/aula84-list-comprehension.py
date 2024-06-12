# List comprehension em Python
# List comprehension é uma técnica para criar listas em um único passo usando sintaxe concisa e eficiente.


import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero * 2)
# print (lista)

# lista2 = [numero * 2 for numero in range(10)]
# print(lista2)

#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

print(produtos, sep='\n') 
# EMPACOTADA
#[{'nome': 'p1', 'preco': 20}, {'nome': 'p2', 'preco': 10}, {'nome': 'p3', 'preco': 30}] 

print(*produtos, sep='\n')
print ('-------------------------------------')
# DESEMPACOTADA
# {'nome': 'p1', 'preco': 20}
# {'nome': 'p2', 'preco': 10}
# {'nome': 'p3', 'preco': 30}

novos_produtos = [produto for produto in produtos]

print(*novos_produtos, sep='\n')
print ('-------------------------------------')
# DESEMPACOTADA
# {'nome': 'p1', 'preco': 20}
# {'nome': 'p2', 'preco': 10}
# {'nome': 'p3', 'preco': 30}

novos_produtos = [{'nome': produto['nome'], 'preco': produto['preco'] * 1.5} for produto in produtos]
print(*novos_produtos, sep='\n')
print ('-------------------------------------')

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.5} for produto in produtos]
print(*novos_produtos, sep='\n')
print ('-------------------------------------')

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.5} if produto['preco'] > 20 else {**produto, 'preco': produto['preco']*2} for produto in produtos]
print(*novos_produtos, sep='\n')


#Filtro de dados em list comprehension
lista = [n for n in range(10) if n%2==0]
print ('------------------FILTRO-------------------')
#print(*novos_produtos, sep='\n')
p(lista)


novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.5}
    if produto['preco'] > 20 
    else {**produto, 'preco': produto['preco']*2}
    for produto in produtos 
    if produto['preco']>25
]

print ('------------------FILTRO-------------------')
print(*novos_produtos2, sep='\n')