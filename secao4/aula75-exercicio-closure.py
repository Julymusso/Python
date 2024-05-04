'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o numero recebido como parâmetro.

'''

def cria_funcao(multiplicador):
    def multiplica(numero):
        return multiplicador * numero
    return multiplica

duplica = cria_funcao(2)
triplica = cria_funcao(3)
quadruplica = cria_funcao(4)

print(duplica(10))
print(triplica(20))
print(quadruplica(30))