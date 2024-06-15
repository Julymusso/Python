# Genrator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) #iterator = iterable.__iter__() # tem __iter__ e __next__

# print(next(iterator)) # Eu
# print(next(iterator)) # tenho
# print(next(iterator)) # __iter__
# print(next(iterator))
# Iterator só sabe te entregar o próximo valor

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

# print(lista)
# print(generator)

print(sys.getsizeof(lista)) #85176b na mem
print(sys.getsizeof(generator)) #104b na mem

#DIFERENÇA
#Na lista fica armazenado todos os valores de uma vez.
# O generator fica esperando solicitar o proximo valor. Utiliza o iterator.
# É como se fosse um apontamento para a proxima posição de memória.
# Estrutura de dados, pilha