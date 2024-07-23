# Atributos de classes

class Pessoa:
    #atributo = 'valor'
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    



p1 = Pessoa('João', 25)
p2 = Pessoa('Maria', 30)

print(Pessoa.ano_atual)

Pessoa.ano_atual = 2023

print(Pessoa.ano_atual)

print(f'{p1.nome} tem {p1.idade} anos e nasceu em {p1.get_ano_nascimento()}')
print(f'{p2.nome} tem {p2.idade} anos e nasceu em {p2.get_ano_nascimento()}')