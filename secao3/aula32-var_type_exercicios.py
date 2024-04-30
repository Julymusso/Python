"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Solução 1
""" 
numero_int = input("Insira um número inteiro: ")

if numero_int.isdigit():
    numero_int=int(numero_int)
    par_impar = numero_int % 2 == 0
    par_impar_texto = "ímpar"

    if par_impar:
        par_impar_texto = "par"

    print(f"O número {numero_int} é {par_impar_texto}")
else:
    print("Você não digitou um número inteiro")

"""

# Solução 2
try:
    numero_int = int(input("Insira um número inteiro: "))
    if (numero_int % 2) == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except:
    print("O valor inserido não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora=int(input("Que horas são? (Somente número inteiro) "))
dia=hora >= 0 and hora <= 11
tarde=hora > 11 and hora <= 17
noite=hora > 17 and hora <= 23

try:
    if dia:
        print("Bom Dia!")
    elif tarde:
        print("Boa Tarde!")
    elif noite:
        print("Boa Noite!")
    else:
        print("O dia só tem 24h")
except:
    print("Esse programa só aceita números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome=input("Escreva seu nome: ")

curto=len(nome)<=4
normal=len(nome)>=5 and len(nome)<=6
grande=len(nome)>6

if curto:
    print("Seu nome é curto")
elif normal:
    print("Seu nome é normal")
elif grande:
    print("Seu nome é muito grande")