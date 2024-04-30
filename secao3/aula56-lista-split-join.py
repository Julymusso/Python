"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_palavras_fixed = []
for i, frase in enumerate(lista_palavras):
    lista_palavras_fixed.append(lista_palavras[i].strip())
print(lista_palavras_fixed)

'''
strip() - remove espaços antes e depois
lstrip() - remove espaços a esquerda
rstrip() - remove espaços a direita
'''
