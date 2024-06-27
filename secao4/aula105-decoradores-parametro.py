# Decoradores com parâmetros
#Funçao aninhada mais interna é a que substitui a funçao real
# Funçao decoradora tem que receber uma funcao como parametro

def decoration_factory(a=None,b=None,c=None):
    def function_factory(func):
        print('Decorada 1')

        def aninhada(*args, **kwargs):
            print(f'Parâmetros: {a}, {b}, {c}')
            print('Aninhada 1')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return function_factory

@decoration_factory(1,2,3)
def soma(x, y):
    print(x + y)

multiplica = decoration_factory()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)