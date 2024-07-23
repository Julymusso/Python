# Métodos de classes + factories (fabricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância primeiro
# parâmetro, recebermos a próprria classe.

class Pessoa:
    #atributo = 'valor'
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Sou um método de classe')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonimo', idade)

print(Pessoa.ano_atual)
p1=Pessoa('Joao',21)
p1.metodo_de_classe()
Pessoa.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos('Ana')
print(p2.nome, p2.idade)

p3 = Pessoa.criar_sem_nome(25)
print(p3.nome, p3.idade)