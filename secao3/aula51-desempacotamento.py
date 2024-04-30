"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

_, nome2, *_outras_nomes, _ultimo_nome = ['Maria', 'Helena', 'Carlos', 'Luiz']
print(outras_nomes)