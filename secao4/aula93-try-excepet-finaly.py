# Try, except, else, finally

a = 18
b = 0
#c = a/b

try:
    d = a/b
except ZeroDivisionError:
    print ('Dividiu por zero')

except NameError:
    print ('Variavel nao definida')

except (TypeError, IndexError) as error: #error nesse caso é o nome da variavel. Poderia ter colocado morango.
    print ('Erro de tipo')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
    
except Exception: #Maior classe de excecao do Python. Trata qualquer erro.
    print ('Erro desconhecido')

print("Continue...")