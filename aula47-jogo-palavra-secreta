"""
Faça um jogo para o usuário qual a palavra secreta.
- Você vai propor dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai verificar se ela está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça contagem de tentavisa do seu usuário.
"""

import os
palavra_secreta = 'imprescindivel'
tentativas = 0
palavra_formatada = (len(palavra_secreta) * "*")

while True:
    resposta=input("Você gostaria de tentar adivinhar a palavra secreta? (S/N) ").upper()
    if resposta!="S":
        print("Até mais!")
        exit()
    else:
        print("REGRAS:\n-Só pode digitar uma letra por vez.\nSe a palavra possuir acento, basta ignora-lo.\n-Se a palavra possuir cidilha, substitua pela letra 'C'.\n-Se palavra possuir hífen, utilize-o.\n-Não tem limite de tentativas.\n-Se quiser do jogo, basta digitar 'sair'.")
        print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
        
        while palavra_formatada != palavra_secreta.lower():
            tentativas += 1
            letra = input("Digite uma letra: ").lower()
            os.system('clear')
            #Para sair do jogo, basta digitar 'sair'.
            if letra == 'sair':
                print("Até mais!")
                exit()
            
            #Verifica se uma tentativa de acertar a palavra secreta.
            if len(letra) > 1:
                if letra == palavra_secreta:
                    break
                else:
                    print("VOCÊ ERROU! :(\nContinue tentando!")
                    print(palavra_formatada)
                    continue
                    
            #Verifica se a letra digitada está na palavra secreta.
            if letra in palavra_secreta:
                i = 0
                while i < len(palavra_secreta):
                    if letra == palavra_secreta[i]:
                        palavra_formatada = palavra_formatada[:i] + letra + palavra_formatada[i+1:]
                    i += 1
            print(palavra_formatada)


        print(f'PARABÉS!!! VOCÊ ACERTOU A PALAVRA SECRETA APÓS {tentativas} tentativas.')