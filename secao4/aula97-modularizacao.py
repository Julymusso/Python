# Entendendo os meus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar um módulo inteiro ou parte do módulo
# O pyhton conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece módulos acima do nível do __main__ por padrao.
# O python conhece todos os módulos e pacotes presentes no caminho de sys.path

# import sys
# sys.path.append('/home')

# import aula97_m #Importa o módulo inteiro


# print('Este módulo se chama',__name__) #Este módulo se chama __main__
# print(*sys.path, sep='\n')

import aula97_m
from aula97_m import variavel_modulo, soma

print(variavel_modulo)
print(soma(2, 3))

print(aula97_m.variavel_modulo)
print(aula97_m.soma(2, 3))