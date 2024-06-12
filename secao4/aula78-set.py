'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.html
Respresentados graficamente pelo diagrama Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor inteiro.
'''

'''
Criando um set
set (iterável) ou {1, 2, 3}
'''
s1 = set() #criar set vazio dessa forma
s2 = {'Juliana',1,2,3} #criar set com dados
print(s1, type(s1))
print(s2, type(s2))


'''
Sets são eficientes para remover valores duplicados de iteráveis.
- eles não tem indexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)
'''
s3 = {1,2,3,3,3,3,4,5,6}
print (s1) # ={1,2,3}

'''
Métodos úteis:
add, update, clear, discard
'''

s4 = set()
s4.add(1)
s4.add('Juliana')
s4.update(('Hello World', 3, 4, 1, 4))
s4.clear() # limpa tudo
s4.discard(4) # se o 4 estiver no set, o remove, se não, não faz nada
print(s4)

''''
Operadores úteis:
união | união (union) - Une
intersecção e (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set esquerdo
diferença simétrica ^ - Itens que não estão em ambos
'''

s5 = {1,2,3}
s6 = {2,3,4}
# união
s7 = s5 | s6
print(s7)
# intersecção
s8 = s5 & s6
print(s8)
# diferença
s9 = s5 - s6
print(s9)
# diferença simétrica
s10 = s5 ^ s6
print(s10)
