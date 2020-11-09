a = 10
b = 20
X = "O valor da soma de A e B é"
Z = "Aaaaaaaaaaaaa"
print("O valor da soma de A e B é",a+b,"e eh isso\n"
"Eh us guri")
print("Ser ou não ser\n")
'''Siga adiante'''
print("Naruto")
print (X,a+b,Z)
print ("Temos que",a+b,"é um número, então eh isso valeu",sep=":::::")

comparacao = (a == b)
print("1) a é igual a b", comparacao)

comparacao = (a < b)
print("2) a é menor que b", comparacao)

comparacao = (a >= b)
print("3) a é maior ou igual a b", comparacao)

salario = 1250
idade = 19
resultado = (salario > 1500 and idade >= 18)
print("O resultado da comparação é", resultado)

print(len(X))
print(X[6])

soma_de_a_e_b = a + b
print(soma_de_a_e_b)

nome = input("Informe seu nome: ")
print("Então seu nome é ",nome,", que merda hein",sep="")

numero = int(input("Digite um número inteiro para somar com a: "))
somita = numero + a
print("A soma de A com seu número é:",somita)

numero2 = float(input("Digite um número para somar com a: "))
somita2 = numero2 + a
print("A soma de A com seu número é:",somita2)

Y= "André"
print("Eu tenho %d melões, então %s vai ter todos" %(a,Y))
print("%03d e %2d e %02d e [%003d]" %(a,a,a,a))
c=22.55
print("Isso tem %fcm ou melhor %.0f ou %.1f ou %.2f %.3f"%(c,c,c,c,c))
print("Tenho %.2f%% de certeza"% a)
print("{} tem quase {} anos de idade mas daqui a pouco terá {} mesmo".format(Y,b,b))
print("{0} tem quase {1} anos de idade mas daqui a pouco terá {1} mesmo".format(Y,b))

print(f"O meu nome é {Y}")


email="andrelimarodel@gmail.com"
indice_arroba = email.index("@")
usuario = email[0:indice_arroba]
print("O seu nome de usuário é:",usuario)
'''[0:0:0] inicio do indice(ponto 0), fim do indice(será a letra anterior a colocada) e pulo de letras'''
usuario = email[0:indice_arroba:2]
print("Ou também seu nome de usuário é:",usuario)

indice_ponto = email.index(".")
provedor = email[indice_arroba+1:indice_ponto]
print("Seu provedor é:", provedor)

usuario2, dominio = email.split("@")
indice_ponto2 = dominio.index(".")
provedor2 = dominio[0:indice_ponto2]
print("O usuário é:", usuario2)
print("O provedor é:", provedor2)

d = 7256103.39
print(f"{c:,.2f} e {d:,.1f} ou {d:.2f}")