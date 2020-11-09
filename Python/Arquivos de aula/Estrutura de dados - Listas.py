lista = [0,2,58,6,1, ['Maçã', 'Banana', 'Abacaxi']]
print(lista)

frutas = lista[5]
print(frutas)

soma = lista[0] + lista[1] + lista[2]
print(soma)

letras = ['a','b','c','d']
numeros = [1,2,3]
mistura = [letras, numeros]
print(mistura)
print(mistura[0])
print(mistura[1])

tamanho = len(letras)
print(tamanho)

print(letras.index('c'))

linguagens = ['JAVA', 'PYTHON', 'GO', 'PASCAL', 'C', 'JAVASCRIPT']
linguagem = input("Informe a linguagem: ")
if linguagem.upper() in linguagens:
    print(f"{linguagem.upper()} está na lista")
else:
    print(f"{linguagem.upper()} não está na lista")

listo = []
while True:
    numero = int(input("Digite um número inteiro (informe 0 para sair): "))
    if numero == 0:
        break
    listo.append(numero)
     
for num in listo:
    print(num)