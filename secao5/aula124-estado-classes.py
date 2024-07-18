# Mantendo estado dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            return f'{self.nome} já está filmando'
        else:
            self.filmando = True
            return f'{self.nome} está filmando'
        
    def parar_filmar(self):
        if self.filmando:
            self.filmando = False
            return f'{self.nome} parou de filmar'


    def fotografar(self):
        if self.filmando:
            return f'{self.nome} não pode fotografar filmando'
        else:
            return f'{self.nome} está fotografando'
        
c1 = Camera('Canon',True)
print(c1.filmar())
print(c1.filmando)
print(c1.fotografar())
print(c1.parar_filmar())
print(c1.filmando)
print(c1.fotografar())

c2 = Camera('Nikon')
print(c2.filmando)
print(c2.fotografar())