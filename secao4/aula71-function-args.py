'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
** - **kwargs (empacotamento e desempacotamento)

'''

# x, y, *resto = 1, 2, 3, 4
# print (x, y, resto)

# def soma (x,y):
#     return x + y

def soma (*args):
    total = 0
    print(args)
    for numero in args:
        total += numero
    return total

# print(soma(1, 2, 3, 4, 5))

numeros = 1,2,3,4,5,6,7,8,9
valor = soma(*numeros)
valor2 = soma(numeros)

print(sum(numeros))