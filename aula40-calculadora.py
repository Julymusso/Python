""""
Calculadora
"""
print("Vou te ajudar a calcular!")

while True:
    numero1=input("Insira o primero número da operaçao:\n")
    numero2=input("Insira o segundo número da operaçao:\n")
    operador=input("Insira o tipo da operaçao (+ - / *):\n")
    
    numero_valido = None

    try:
        numero1=float(numero1)
        numero2=float(numero2)
        numero_valido = True
    except:
        numero_valido = None
        
    if numero_valido is None:    
        print("Um ou mais números inseridos é inválido\n")
        continue
    
    operador_permitido = "+-/*"
        
    if operador is not operador_permitido:    
        print("Operador inválido\n")
        continue

    if operador > 1:    
        print("Innsira apenas um operador\n")
        continue

    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
        print("Numero ou operador inválido")

    print(f"{numero1:.2f} {operador} {numero2:.2f} = {resultado:.2f}\n\n")
    sair = input("Deseja realizar outra operação [S]air?").lower().startswith("s")
    if sair:
        break