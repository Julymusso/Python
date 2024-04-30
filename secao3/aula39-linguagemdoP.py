"""
Iterando com strings com while
"""
#Linguagem do P

nome=input(f"Insira um nome para traduzi-lo para a língua do P \n").lower()
i = 0
nome_traduzido = ""

while i < len(nome):
    if nome[i] == " " or nome[i] == "-" or nome[i] == "_":
        nome_traduzido = nome_traduzido + nome[i]
        i += 1
        continue
    else:
        if nome[i] == "a" or nome[i] == "e" or nome[i] == "i" or nome[i] == "o" or nome[i] == "u":
            if nome[i-1] != "a" or nome[i-1] != "e" or nome[i-1] != "i" or nome[i-1] != "o" or nome[i-1] != "u":
                nome_traduzido = nome_traduzido + nome[i] + "P" + nome[i]
                i += 1
            else:
                nome_traduzido = nome_traduzido + nome[i] + "P" + nome[i]
        else:
            nome_traduzido = nome_traduzido + nome[i]
            i += 1
print(nome_traduzido)