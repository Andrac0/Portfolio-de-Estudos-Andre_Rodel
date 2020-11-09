lista_pares = []
lista_impares = []
while True:
    numero = int(input("Digite um número(Nº 0 para sair): "))
    if numero == 0:
        break
    if numero %2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    
lista_pares.sort()
lista_impares.sort()

print(f"O número pares são: {lista_pares}")
print(f"O número impares são: {lista_impares}")