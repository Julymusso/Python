nome = 'Juliana Musso'
altura = 1.65
peso = 95

# ... -> place holder. Ao rodar o código não gera erro, mesmo sem valor definido para a variável
#icm = ... #peso / (altura x altura)

imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura e pesa', peso,  'kg. Possui icm igual a', imc)