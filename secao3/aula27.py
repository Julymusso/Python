"""
Fatiamento de strings
   012345678
   Ola mundo
(-)987654321
Fatiamento [i:f:p] [::]
Obs.: a func len retorna a quantidade de caracter da str
"""

var = "Ola Mundo"
print(var[4:])
#Mundo
print(var[2:7])
#a Mun
print(var[:3])
#Ola
print(var[2:6:2])
#aM
print(len(var))
#9