"""
Iterável -> str, range, etc (__inter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador (me entrega um objeto que sabe interar na string)
"""

"""texto = 'Luiz'.__iter__() = iter('Luiz')"""
"""texto.__next__() = next(texto)"""

# for letra in texto:

texto = 'Luiz' #iteravel
iterador = iter(texto) #iterator

#Isso é como o for funciona por debaixo do pano
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break



for letra in texto:
    print(letra)