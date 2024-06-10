'''
Sistemas de perguntas e respostas
'''
import os

perguntas = [
    {
        'pergunta': 'Qual a capital do Brasil?',
        'opcoes': ['Rio de Janeiro','São Paulo','Brasília','Curitiba'],
        'correta': 'Brasília'
    },
    {
        'pergunta': 'Qual o maior time do mundo?',
        'opcoes': ['Real Madrid','Barcelona','Juventus','Manchester United'],
        'correta': 'Manchester United'
    },
]


#Função jogar

def jogar():
    os.system('clear')
    pontos = 0
    for questao in perguntas:
        print(questao['pergunta'])
        for op in questao['opcoes']:
            print(op['opcoes'])
        resposta=input()
        if resposta == questao['correta']:
            print('Você acertou!')
            pontos += 1
        else:
            print('Que pena, você errou. Tente outra questão!')
    return pontos


menu = '''
1 - Jogar
2 - Inserir pergunta
3 - Sair
'''

while True:
    menu_opcao = input(menu)
    if menu_opcao == '1':
        pontos = jogar()
        print (f'Parabéns, você acertou {pontos} de {len(perguntas)}') if pontos != 0 else print('Você nâo pontuou dessa vez')
    elif menu_opcao == '2':
        print('Inserindo pergunta...')
    else:
        print('Até a próxima!')
        break