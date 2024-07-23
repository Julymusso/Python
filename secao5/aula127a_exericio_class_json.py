# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('João', 'Silva')
p2 = Pessoa('Maria', 'Santos')
p3 = Pessoa('Pedro', 'Souza')
p4 = Pessoa('Ana', 'Oliveira')
p5 = Pessoa('Lucas', 'Fernandes')
p6 = Pessoa('Juliana', 'Pereira')

pessoa = [vars(p1),vars(p2),vars(p3),vars(p4),vars(p5),vars(p6)]


FILE_PATH = '/home/juliana/OneDrive/Estudos/Cursos Udemy/Python/curso_python/secao5/aula127a.json'

def salvar():
    with open(FILE_PATH,'w+') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)
    print('La la land')

if __name__ == '__main__':
    salvar()