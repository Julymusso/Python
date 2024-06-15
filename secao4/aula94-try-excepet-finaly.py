# Try, except, else, finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print(1)
    #a = 10/1
    a = 10/0
except ZeroDivisionError:
    print(3)
finally: # Semprer será executado, independente do que acontecer no try
    print(2)