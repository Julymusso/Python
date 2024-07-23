# @property - um getter no modo Pythonico
# getter - um método para obter um atributo
# modo pythonico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo

#Código cliente é o código que usa o seu código

class Caneta:
    # def __init__(self, cor):
    #     #private protect public (em outras linguagens) -  encapsulamento
    #     self.cor = cor

    def __init__(self, cor):
    #private protect public (em outras linguagens) -  encapsulamento
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta

    def get_cor(self):
        return self.cor
    
    @property
    def cor_tampa(self):
        return ('Cor da Tampa')

caneta = Caneta('Azul')

print(Caneta.get_cor(caneta))
print(caneta.cor)
print(caneta.cor_tampa)