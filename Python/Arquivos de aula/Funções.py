<<<<<<< HEAD
def soma():                             #Todas as váriaveis dentro destas funções são locais
    num1 = 12                           #Ou seja não são acessadas por fora
    num2 = 25
    total = num1 + num2
    print(f"Total: {total}")
soma()

def soma2(numero1, numero2):
    total = numero1 + numero2
    print(f"Total: {total}")
soma2(10, 20)

def soma3(n1, n2):
    total = n1 + n2
    return total
miranha = soma3(10, 21)
print(f"Soma: {miranha}")

print(f"Soma: {soma3(5, 11)}")

def maior_valor(valores):
    return max(valores)
def capturar_numeros():
    lista_numeros = []
    while True:
        numero = int(input("Informe um número inteiro ou zero para sair: "))
        if numero == 0:
            break
        lista_numeros.append(numero)
    return maior_valor(lista_numeros)
print(f"Maior valor: {capturar_numeros()}")

valor1 = 10
valor2 = 30
def mandarim():
    global valor1       #Esta variável se tornou global
    valor1 = 20
    valor2 = 40
    print(f"O valor1 dentro da função é {valor1} e o valor2 é {valor2}")
print(f"{valor1}")
mandarim()
print(f"{valor1}")
print(f"{valor2}\n")

#Váriaveis globais tendem a não ser muito utilizadas pois recomendase que não as altere
#além de que por padrão devem ser escritas com letras maiúsculas

print(f"Variáveis Globais: {globals()}\n")
print(f"Variáveis Locais: {locals()}\n") #Mostra as funções de cada tipo

def soma4(valor1, valor2, imprime = False): #parametros opcionais no final
    resultado = valor1 + valor2
    if imprime:
        print(f"Soma: {resultado}")
        return resultado
total1 = soma4(74, 47, True)    #Visto que está falso na declaração ele não ira imprimir
                                #Caso não esteja declarado "True"
def soma5(a1, a2, imprime = False):
    print(f"Valor 1: {a1}")
    print(f"Valor 2: {a2}")
    resultado = a1 + a2

    if imprime:
        print(f"Soma: {resultado}")
        return resultado
total = soma5(a2 = 90, a1 = 20, imprime = True)
total = soma5(a2 = 90, a1 = 20, imprime = False)
total = soma5(a2 = 90, a1 = 20)

def soma6(num1, num2):
    return num1 + num2
def multiplicacao(num1, num2):
    return num1 * num2
def calcular(funcao, num1, num2):
    return funcao(num1, num2)
total_soma=calcular(soma6, 10, 20)
total_multiplicacao=calcular(multiplicacao, 10, 20)

print(f"Total da soma: {total_soma}")
print(f"Total da multiplicação: {total_multiplicacao}")

def soma7(a1, a2, imprime = False):
    print(f"Valor 1: {a1}")
    print(f"Valor 2: {a2}")
    resultado = a1 + a2

    if imprime:
        print(f"Soma: {resultado}")
        return resultado
lista = [49, 42, True]
print(f"Soma com lista: {soma7(*lista)}") 

def soma8(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"Soma: {total}")
        return total
x = soma8(True, 10,20,30,40,50,60,70)
=======
def soma():                             #Todas as váriaveis dentro destas funções são locais
    num1 = 12                           #Ou seja não são acessadas por fora
    num2 = 25
    total = num1 + num2
    print(f"Total: {total}")
soma()

def soma2(numero1, numero2):
    total = numero1 + numero2
    print(f"Total: {total}")
soma2(10, 20)

def soma3(n1, n2):
    total = n1 + n2
    return total
miranha = soma3(10, 21)
print(f"Soma: {miranha}")

print(f"Soma: {soma3(5, 11)}")

def maior_valor(valores):
    return max(valores)
def capturar_numeros():
    lista_numeros = []
    while True:
        numero = int(input("Informe um número inteiro ou zero para sair: "))
        if numero == 0:
            break
        lista_numeros.append(numero)
    return maior_valor(lista_numeros)
print(f"Maior valor: {capturar_numeros()}")

valor1 = 10
valor2 = 30
def mandarim():
    global valor1       #Esta variável se tornou global
    valor1 = 20
    valor2 = 40
    print(f"O valor1 dentro da função é {valor1} e o valor2 é {valor2}")
print(f"{valor1}")
mandarim()
print(f"{valor1}")
print(f"{valor2}\n")

#Váriaveis globais tendem a não ser muito utilizadas pois recomendase que não as altere
#além de que por padrão devem ser escritas com letras maiúsculas

print(f"Variáveis Globais: {globals()}\n")
print(f"Variáveis Locais: {locals()}\n") #Mostra as funções de cada tipo

def soma4(valor1, valor2, imprime = False): #parametros opcionais no final
    resultado = valor1 + valor2
    if imprime:
        print(f"Soma: {resultado}")
        return resultado
total1 = soma4(74, 47, True)    #Visto que está falso na declaração ele não ira imprimir
                                #Caso não esteja declarado "True"
def soma5(a1, a2, imprime = False):
    print(f"Valor 1: {a1}")
    print(f"Valor 2: {a2}")
    resultado = a1 + a2

    if imprime:
        print(f"Soma: {resultado}")
        return resultado
total = soma5(a2 = 90, a1 = 20, imprime = True)
total = soma5(a2 = 90, a1 = 20, imprime = False)
total = soma5(a2 = 90, a1 = 20)

def soma6(num1, num2):
    return num1 + num2
def multiplicacao(num1, num2):
    return num1 * num2
def calcular(funcao, num1, num2):
    return funcao(num1, num2)
total_soma=calcular(soma6, 10, 20)
total_multiplicacao=calcular(multiplicacao, 10, 20)

print(f"Total da soma: {total_soma}")
print(f"Total da multiplicação: {total_multiplicacao}")

def soma7(a1, a2, imprime = False):
    print(f"Valor 1: {a1}")
    print(f"Valor 2: {a2}")
    resultado = a1 + a2

    if imprime:
        print(f"Soma: {resultado}")
        return resultado
lista = [49, 42, True]
print(f"Soma com lista: {soma7(*lista)}") 

def soma8(imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"Soma: {total}")
        return total
x = soma8(True, 10,20,30,40,50,60,70)
>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
print(x)