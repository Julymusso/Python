#--------------------------------------------------------------
"""
(Caractere)(><)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o numero aparecer antes dos zeros
Sinal - + ou -
Ex,: 0>-100,.f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
#       ABC
print(f"{variavel:#<5}")
#ABC##
print(f"{variavel:-^15}")
#------ABC------
print(f"{1000.8766756986879698:0=+10,.1f}")
#+001,000.9
print(f"O hexadecimal de 1500 é {1500:08X}")
#O hexadecimal de 1500 é 000005DC
