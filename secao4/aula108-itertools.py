# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1,'__iter__'))
print('c1', hasattr(c1,'__next__'))
print('r1', hasattr(r1,'__iter__'))
print('r1', hasattr(r1,'__next__'))

#Ou seja count é interavel e iterador
#range é somente iteravel