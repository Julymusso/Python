# Métodos em instâncias de classes Python

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self,alimento):
        print(f'{self.nome} está comendo {alimento}')

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

leao = Animal('Simbar')
print(leao.nome)
leao.comendo('capim')
leao.executar('mamão')
