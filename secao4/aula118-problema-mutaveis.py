# Problema dos paametrros mutaveis em funções Python
# Mutáveis: listas, dicionários e objetos
# Imutáveis: int, float, string, bool e tupla
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# cliente1 = adiciona_clientes('João')
# adiciona_clientes('Maria', cliente1)
# print(cliente1) #['João', 'Maria']

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Pedro', cliente2)
# print(cliente2) #['João', 'Maria', 'Helena', 'Pedro']

#soluçao 1
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# lista1 = []
# cliente1 = adiciona_clientes('João', lista1)
# adiciona_clientes('Maria', cliente1)
# print(cliente1) #['João', 'Maria']

# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Pedro', cliente2)
# print(cliente2) #['Helena', 'Pedro']

#soluçao 2
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('João')
adiciona_clientes('Maria', cliente1)
print(cliente1) #['João', 'Maria']

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Pedro', cliente2)
print(cliente2) #['Helena', 'Pedro']

#Se o parametro for mutável, não colocar valor fixo