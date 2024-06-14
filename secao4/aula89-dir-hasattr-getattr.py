# dir, hasattr, getattr em Python
# dir - no modo debug, em debug console dir(var)
string = 'Juliana'
metodo = 'upper'

print (string)

if hasattr(string, metodo): #(var, metodo)
    print('Existe upper')
    print(string)

    print(getattr(string, metodo)()) #JULIANA
else:
    print('Não existe o método', metodo)