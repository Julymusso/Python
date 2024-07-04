#O trabalho dessa função será unir duas listas na ordem.
#Use todos os valores da menor lista
#Ex.: ['Salvador', 'Ubatuba','Rio de Janeiro', 'Belo Horizonte']
#['BA','SP','MG','RJ']
#Resultado
#[('Salvador','BA'), ('Ubatuba','SP'), ('Belo Horizonte','MG')]


# def zipper(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo)]
#     # return [
#     #     for i in range(intervalo)
#     #         lista1[i], lista2[i]
#     # ]
   
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA','SP','MG','RJ']

# print(zipper(l1,l2))

# from itertools import zip_longest

# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA','SP','MG','RJ']

# print(list(zip(l1, l2)))
# print(list(zip_longest(l1,l2,fillvalue='SEM CIDADE')))


#---------------------------------------------||---------------------------------------

#Considerando duas listas de inteiros ou floats some os valores nas listas retornando uma nova lista com os valores somados:
#Se uma lista for maior que a outra, a soma é realizada apenas até o tamanho da menor.
#Ex.: a = [1, 2, 3, 4, 5]
#b = [6, 7, 8, 9, 10]
#Resultado
#[7, 9, 11, 13, 15]

# def soma_listas(lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [(lista1[i] + lista2[i]) for i in range(intervalo)]

# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 10]

# print(soma_listas(l1, l2))

#---------------------------------------------||---------------------------------------