﻿# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


print(criar_funcao(soma, 5)(4))
print(criar_funcao(multiplica, 10)(6))
















soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(4))
print(multiplica_por_dez(5))