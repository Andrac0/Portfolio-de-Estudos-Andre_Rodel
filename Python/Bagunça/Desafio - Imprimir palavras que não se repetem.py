lista_palavras = []
lista_palavras_final = []
while True:
    palavras = input("Digite uma palavra(Nº 0 para sair): ")

    if palavras == "0":
        break
    else:
        lista_palavras.append(palavras)

for palavras in lista_palavras:
    if lista_palavras.count(palavras) == 1:
        lista_palavras_final.append(palavras)

print(lista_palavras_final)