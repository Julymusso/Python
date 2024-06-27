def decorator_parameter(name):
    def decorator(func):
        print('Decorator:', name)

        def new_function(*args, **kwargs):
            answer = func(*args, **kwargs)
            final = f'{answer} {name}'
            return final
        return new_function
    return decorator

@decorator_parameter(name='third')
@decorator_parameter(name='second')
@decorator_parameter(name='first')
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)