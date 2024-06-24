# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def create_function(func):
    def internal(*args, **kwargs):
        print('Função será decorada')
        for arg in args:
            is_string(arg)
        print(f'O resultado é {func(*args, **kwargs)}')
        print('Função decorada, mas não executada ainda')
        return func(*args, **kwargs)
    return internal

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')

inverte_string_checa_param = create_function(inverte_string)

print(inverte_string_checa_param('Juliana'))
print('Agora foi executado')
