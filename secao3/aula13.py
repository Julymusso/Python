nome = 'Juliana Musso'
altura = 1.65
peso = 95

# ... -> place holder. Ao rodar o código não gera erro, mesmo sem valor definido para a variável
#icm = ... #peso / (altura x altura)

imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f}cm de altura'
linha_2 = f'e pesa {peso}kg e seu imc é {imc:.2f}'


print(linha_1, linha_2)
