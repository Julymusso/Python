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
# Por convenção, atributos iniciados por "_" dentro da classe, não devem ser utilizados no código

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor
    
#     @property
#     def cor(self):
#         print('PROPERTY')
#         return self.cor_tinta

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        #self.cor = cor #configura o setter ja no instanciamento do objeto
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self,valor):
        self._cor_tampa = valor

    
caneta = Caneta('Azul')
caneta.cor_tampa = ('Branco')
print(caneta.cor)
print(caneta.cor_tampa)

caneta1 = Caneta('Rosa')
caneta1.cor_tampa = ('Lilas')
# GETTER -> obter vaor
print(caneta1.cor)
print(caneta1.cor_tampa)