"""
Faça uma lista de compras com listas
O usuário deve ter a opção de adicionar, remover e listar os itens da lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os
lista=[]

while True:
    print('Selecione uma opção')
    opcao=input('[i]nserir  [r]emover  [l]istar [s]air\n').lower()
    os.system('clear')
    if opcao == 's':
        exit()
    elif opcao == 'l':
        if len(lista) == 0:
            print('A lista está vazia')
        else:
            for indice, item in enumerate(lista):
                print(f'{indice} - {item}')
    elif opcao == 'i':
        item = input('Digite o item a ser inserido: ')
        lista.append(item)
        print('Item inserido com sucesso')
    elif opcao == 'r':
        item_deletar = input('Digite o item a ser deletado: ')
        
        for indice, item in enumerate(lista):
            if item == item_deletar or indice == int(item_deletar):
                lista.remove(item)
                print('Item deletado com sucesso')                
            else:
                print('Item não encontrado')
    else:
        print('Opção inválida')
