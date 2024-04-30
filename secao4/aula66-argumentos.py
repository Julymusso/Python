'''
Argumentos nomeados e não nomeados em função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) = Argumento posicional
'''

def soma(x, y, z):
    #Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y =', x + y)

#print(soma) #Mostra posição da função na memória
soma(1, 2, 3)
soma(y=2, x=1, z=3)
soma(1, 2, z=3)