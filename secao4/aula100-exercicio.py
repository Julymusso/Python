# copy, sorted, produtos.sort
# Exercícios


import copy

from exercicios.dados import produtos

print('-----------------------PRODUTOS-------------------------')
print (*produtos, sep='\n')


# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)

# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
    {'nome':item['nome'],'preco': round(item['preco'] * 1.1, 2)} 
    for item in novos_produtos]

print('\n-----------------------NOVOS PRODUTOS-------------------------')
print (*novos_produtos, sep='\n')



# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
produtos_ordenados_por_nome.sort(key=lambda item: item['nome'], reverse=True)

print('\n-----------------------PRODUTOS ORDENADOS POR NOME-------------------------')
print (*produtos_ordenados_por_nome, sep='\n')



# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(produtos)

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco.sort(key=lambda item: item['preco'])

print('\n-----------------------PRODUTOS ORDENADOS POR PRECO-------------------------')
print (*produtos_ordenados_por_preco, sep='\n')

print('\n-----------------------PRODUTOS-------------------------')
print (*produtos, sep='\n')