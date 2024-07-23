# @staticmethod são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self enm ao cls.
#Em resumo, são funções que existem dentro da sua classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi!')