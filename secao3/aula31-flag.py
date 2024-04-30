""" Flag - Marcar um local
Nome = Não valor
Funçao id() - mostra local em memoria da variavel
id = identidade
is e is not - é ou não é (tipo, valor, identidade) """

v1 = 'a'
print(id(v1))
# 140512720520688

condicao = True
# Faça algo
# True False
# True True

#condicao = False
# Faça algo
# None True
# None False

passou_no_if = None
if condicao:
   passou_no_if = True
   print('Faça algo')
else:
   print('Não faça algo')
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

