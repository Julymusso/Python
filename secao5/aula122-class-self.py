# Métodos em instâncias de classes Python

class Carro:
    def __init__(self, nome):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} acelerou')
        

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar() # Atributo de instância

Carro.acelerar(fusca) # Atributo de classe

celta = Carro('Celta')
print(celta.nome)
fusca.acelerar() # Atributo de instância