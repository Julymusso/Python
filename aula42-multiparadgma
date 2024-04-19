frase = 'O Python é a linguagem de progração'\
    'multiparadigma.' \
    'Python foi criado por Guido Van Rossum.'

i=0
letra_mais_apareceu = 0
quantidade_vezes_letra_mais_apareceu = 0
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i+=1
        continue

    quantidade_vezes_letra_apareceu = frase.count(letra_atual)

    if quantidade_vezes_letra_apareceu > quantidade_vezes_letra_mais_apareceu:
        letra_mais_apareceu = letra_atual.upper()
        quantidade_vezes_letra_mais_apareceu = quantidade_vezes_letra_apareceu

    i+=1
    
    #print(letra_atual," :", quantidade_vezes_letra_apareceu)

print('A letra que apareceu mais vezes foi '
      f'{letra_mais_apareceu} que apareceu '
    f'{quantidade_vezes_letra_mais_apareceu} vezes')