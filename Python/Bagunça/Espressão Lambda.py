<<<<<<< HEAD
b = lambda x: x**2  #O duplo "**" faz a potencia do número
print(b(4))

dobrar2= lambda x: x*2
print("O dobro do valor de vinte é: ", dobrar2(20))

multiplicar = lambda x, y: x*y
print("10 * 80 =", multiplicar(10,8))

def incrementar(n):
    return lambda x: x + n

somar2 = incrementar(2)
somar8 = incrementar(8)

a=1
b=somar2(a)
print(b)
c=somar8(a)
print(c)
d=somar2(10)
print(d)

soma = lambda lista: sum(lista)

numeros = [1,5,10,50]
total = soma(numeros)
print(total)

numeros = [80,74,25]
total = soma(numeros)
print(total)

curso = lambda a = "Curso", b = "Python", c = "para todos!!!": a + " " + b + " " + c
print(curso())

def nomeCompleto():
    completo = lambda nome, sobrenome: nome + " " + sobrenome
    return completo

meuNome = nomeCompleto()
print(meuNome("André", "Lima"))

tabuada = [
    lambda x: f"{x} * 1 = " + str(x * 1),
    lambda x: f"{x} * 2 = " + str(x * 2),
    lambda x: f"{x} * 3 = " + str(x * 3),
    lambda x: f"{x} * 4 = " + str(x * 4),
    lambda x: f"{x} * 5 = " + str(x * 5),
    lambda x: f"{x} * 6 = " + str(x * 6),
    lambda x: f"{x} * 7 = " + str(x * 7),
    lambda x: f"{x} * 8 = " + str(x * 8),
    lambda x: f"{x} * 9 = " + str(x * 9),
    lambda x: f"{x} * 10 = " + str(x * 10)
]

numero = int(input("Informe o número para gerar a tabuada: "))

for x in tabuada:
    print(x(numero))
=======
b = lambda x: x**2  #O duplo "**" faz a potencia do número
print(b(4))

dobrar2= lambda x: x*2
print("O dobro do valor de vinte é: ", dobrar2(20))

multiplicar = lambda x, y: x*y
print("10 * 80 =", multiplicar(10,8))

def incrementar(n):
    return lambda x: x + n

somar2 = incrementar(2)
somar8 = incrementar(8)

a=1
b=somar2(a)
print(b)
c=somar8(a)
print(c)
d=somar2(10)
print(d)

soma = lambda lista: sum(lista)

numeros = [1,5,10,50]
total = soma(numeros)
print(total)

numeros = [80,74,25]
total = soma(numeros)
print(total)

curso = lambda a = "Curso", b = "Python", c = "para todos!!!": a + " " + b + " " + c
print(curso())

def nomeCompleto():
    completo = lambda nome, sobrenome: nome + " " + sobrenome
    return completo

meuNome = nomeCompleto()
print(meuNome("André", "Lima"))

tabuada = [
    lambda x: f"{x} * 1 = " + str(x * 1),
    lambda x: f"{x} * 2 = " + str(x * 2),
    lambda x: f"{x} * 3 = " + str(x * 3),
    lambda x: f"{x} * 4 = " + str(x * 4),
    lambda x: f"{x} * 5 = " + str(x * 5),
    lambda x: f"{x} * 6 = " + str(x * 6),
    lambda x: f"{x} * 7 = " + str(x * 7),
    lambda x: f"{x} * 8 = " + str(x * 8),
    lambda x: f"{x} * 9 = " + str(x * 9),
    lambda x: f"{x} * 10 = " + str(x * 10)
]

numero = int(input("Informe o número para gerar a tabuada: "))

for x in tabuada:
    print(x(numero))
>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
