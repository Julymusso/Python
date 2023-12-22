number1=input("Digite um valor: ")
number2=input("Digite outro valor: ")

if number1 > number2 :
    print(f'{number1} é maior do que {number2}')
elif number2 > number1 :
    print(f'{number2} é maior do que {number1}')
else :
    print(f'{number1} e {number2} são iguais')