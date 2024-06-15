# Introdução Generator functions em Python
# generator = (n for n in range(100))

def generator(n=0):
    yield 1 # Pausar a execução da função
    print('Continuando...')
    yield 2
    print('Pausei de novo')
    yield 2
    print('Agora acabou!')
    return 'Acabou'

# gen = generator(n=0)
# print(gen)
# print(next(gen)) # Pega o primeiro yield
# print(next(gen)) # Pega o segundo yield
# print(next(gen)) # Pega o terceiro yield   
# print(next(gen)) # Para a função. StopIteration
# print(next(gen)) # Não executa nada

def abacaxi(n=0, maximum=10):
    while True:
        yield n
        if n >= maximum:
            return
        n += 1

doce = abacaxi(n=2, maximum=9)
for n in doce:
    print(n)