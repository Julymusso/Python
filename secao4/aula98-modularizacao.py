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

#singleton = só pode existir um unico modulo naquela instancia. 
# python só importa o modulo uma unica vez

import aula98_m
import importlib

print(aula98_m.variavel)

for i in range (10):
    importlib.reload(aula98_m)
    print(i)