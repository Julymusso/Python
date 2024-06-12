# Empacotamento e desempacotamento
""" 
a, b = 1, 2

print(a, b)

a, b = b, a

print(a, b) """

pessoa = {
    'nome' : 'Juliana',
    'sobrenome' : 'Soares'
}

""" (a1, a2), (b1, b2) = pessoa.items()
print(a1, a2, b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor) """


dados_pessoa = {
    'idade' : 18,
    'altura' : 1.80
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

# args e kwargs

# args  (já vimos)

#kwargs - keyword arguments (argumentos nomeados)

def monstro_argumentos_nomeados (*args, **kwargs):
    print(kwargs)

monstro_argumentos_nomeados(nome='Felipe', qlq=123, aba='pai')

monstro_argumentos_nomeados(**pessoa)