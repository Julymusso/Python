"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point...
http://docs/python.org/pt-br/3/tutorial/floatingpoint.tml
"""
import decimal

numero_11 = decimal.Decimal('0.1')
numero_22 = decimal.Decimal('0.7')
print(numero_11 + numero_22)
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')   
print(round(numero_3, 2)) 