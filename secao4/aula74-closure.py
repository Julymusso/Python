'''
Closure e funções que retornem outras funções

'''

def criar_saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar

for nome in ['Maria', 'Juliana', 'Joao']:
    print (criar_saudacao('Bom dia')(nome))
    print (criar_saudacao('Boa tarde')(nome))
    print (criar_saudacao('Boa noite')(nome))


#---------------------------------------||------------------------------------
#---------------------------------------||------------------------------------















#---------------------------------------||------------------------------------
#---------------------------------------||------------------------------------

def criar_saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar
print('\n\n------Dessa forma tambem funciona-----\n\n')

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Juliana', 'Joao']:
    print (falar_bom_dia(nome))
    print (falar_boa_tarde(nome))
    print (falar_boa_noite(nome))


