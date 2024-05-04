'''
Exercícios com funções
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.

'''
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

'''
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar
'''

def impar_par(numero):
    if numero % 2 == 0:
        return True

print(multiplica(1,2,3,4))
print ('Par') if impar_par(9) else print('Impar')