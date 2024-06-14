# isinstance - para saber se o objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [1, 2, 3], (1, 2), {1, 2}, {'nome': 'Luiz'}
]

for item in lista:
    if isinstance(item, set):
        print(item, ': Set')
    elif isinstance(item, int):
        print(item, ': Int')
    elif isinstance(item, str):
        print(item, ': Str')
    elif isinstance(item, float):
        print(item, ': Float')
    elif isinstance(item, bool):
        print(item, ': Bool')
    elif isinstance(item, list):
        print(item, ': List')
    elif isinstance(item, dict):
        print(item, ': Dict')
    elif isinstance(item, tuple):
        print(item, ': Tuple')


# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)