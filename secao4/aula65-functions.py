# # cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# import re
# import sys

# # cpf_enviado_usuario = '746.824.890-70' \
# #     .replace('.', '') \
# #     .replace(' ', '') \
# #     .replace('-', '')
# entrada = input('CPF [746.824.890-70]: ')
# cpf_enviado_usuario = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
# )

# entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_e_sequencial:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')

import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

#PRIMEIRO DÍGITO DO CPF
i=10
soma = 0
for digito in cpf:
    numero = int(digito)*i
    soma += numero
    i -= 1

soma *= 10
resto = soma % 11
if resto < 9:
    cpf=cpf+str(resto)
else:
    cpf=cpf+str(0)

#SEGUNDO DÍGITO DO CPF
i=11
soma = 0
for digito in cpf:
    numero = int(digito)*i
    soma += numero
    i -= 1

soma *= 10
resto = soma % 11
if resto < 9:
    cpf=cpf+str(resto)
else:
    cpf=cpf+str(0)

#COPARE CPF COM CPF VALIDO
print(cpf)