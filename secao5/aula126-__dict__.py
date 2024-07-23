# Atributos de classes

class Pessoa:
    #atributo = 'valor'
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'João', 'idade': 25}
p1 = Pessoa(**dados)


p1 = Pessoa('João', 25)

p1.__dict__['sobrenome'] = 'Silva'
print(p1.__dict__)
print(vars(p1))

print(f'{p1.nome} tem {p1.idade} anos e nasceu em {p1.get_ano_nascimento()}')