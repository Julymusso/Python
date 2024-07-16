# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import os

caminho_arquivo = '/home/juliana/OneDrive/Estudos/Cursos Udemy/Python/curso_python/secao4/aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w+', encoding = 'utf8') as arquivo:
    arquivo.write('Juliana Ricato Musso Silva\n')
    arquivo.write('Jessé Gomes da Silva\n')
    arquivo.write('Atenção\n')
    arquivo.writelines(('linha 3\n', 'linha 4\n'))
    
    arquivo.seek(0,0) #volta o cursor pra inicio do arquivo
    print(arquivo.read())

    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())

#os.remove(caminho_arquivo)
#os.unlink(caminho_arquivo)