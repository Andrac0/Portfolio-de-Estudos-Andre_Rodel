lista_num = []
lista_pares = []
lista_impares = []
soma = 0
tem_mais = False
num_mais = 0
qtd_mais = 1
while True:
    num = float(input("Digite um número(sendo nº 0 para sair): "))
    soma += num
    if num == 0:
        break
    else:
        lista_num.append(num)
    if num %2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(f"O primeiro número informado foi: {lista_num[0]}")
print(f"O ultimo número informado foi: {lista_num[-1]}")
print(f"1 - A soma dos números informados é: {soma}")
print(f"2 - A soma dos números informados é: {sum(lista_num):.2f}")
print(f"1 - A média dos números informados é: {soma/len(lista_num)}")
print(f"2 - A média dos números informados é: {sum(lista_num)/len(lista_num):.2f}")
print(f"Os números pares são: {lista_pares}")
print(f"Os números impares são: {lista_impares}")
print(f"A lista completa é: {lista_num}")
lista_num.reverse()
print(f"Lista em ordem inversa: {lista_num}")
lista_num.sort()
print(f"Lista em ordem crescente: {lista_num}")
for num in lista_num:
    qtd = lista_num.count(num)
    if qtd > qtd_mais:
        num_mais = num
print(f"O número que mais apareceu foi: {num_mais}")