'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas os nomes do mesmo local podem ser alcançados.
'''

#Escopo global
x = 1


def escopo():
    x = 10
    def outra_funcao():
        #Escopo local
        y = 2    
        print(x, y)
    print(x)
    outra_funcao()

escopo()
print(x)


#Escopo global
a = 1


def escopos():
    global a
    a = 10
    def outra_funcao():
        #Escopo local
        b = 2    
        print(a, b)
    print(a)
    outra_funcao()

escopos()
print(a)