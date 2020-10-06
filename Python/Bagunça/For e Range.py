inicio = int(input("Digite o valor de inicio: "))
fim = int(input("Digite o valor de fim: "))
salto = int(input("Digite o valor de salto: "))
texto = "Cálculo: "
soma = 0
for numero in range(inicio, fim, salto):
    texto = texto + str(numero)
    soma = soma + numero
    if numero > 50:
        texto = texto + " Passou de 50"
        break
    if numero != fim-1:
        texto = texto + " + "
print(f"{texto}")
print(f"{soma}")
