'''
Higher Order Functions
Funções de primeira classe

'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

saudacao_2 = saudacao

print (saudacao_2('Bom dia', 'Gabriel'))

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao,'Bom dia', 'Gabriel')
print(v)