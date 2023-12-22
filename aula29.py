"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

""" print(1234)
try:
    int('A')
except:
    print("Não é possível converter caracter para numero inteiro")
print(12334) """

numero_str = input("Vou dobrar o número que você digitar: ")

try:
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.0f}")
except:
    print("Isso não é um número")