# Encapsulamento (modificadorers de acesso: public, protected, private)
# Python não tem modificadores de acesso
# Mas podemos seguir as seguintes convenções
#           (sem underline) = public
#                   pode ser usado em qlq luga
            # _(um underline) = protected
            #         não dever ser usado fora da classe ou suas subclasses
            # __(dois underlines) = private
            #         "name mangling" (desfiguração de nomes) em Python
            # só deve ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido' #deve ser usado somente dentro dessa classe (Foo) ou em classe filhas.
        self.__private = 'isso é privado' #deve ser usado somente dentro dessa classe (Foo). Nao pode em classes filhas
        self._metodo_protected()

    def metodo_publico(self):
        self._metodo_protected()
        return 'método público'
    
    def _metodo_protected(self):
        self.__metodo_private()
        return 'método protected'
    
    def __metodo_private(self):
        return 'método private'


f = Foo()
print(f.public)
print(f.metodo_publico())
# print(f._protected)   #Isso não pode. Apesar do Python permitir, não é convencional. Está errado
# print(f._metodo_protected())   #Isso não pode. Apesar do Python permitir, não é convencional. Está errado
# print(_Foo__metodo_private())  #isso tbm nao deve ser utilizado