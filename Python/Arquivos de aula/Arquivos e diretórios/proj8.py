palavras = []
with open("Arquivos e diretórios/hino nacional.txt", encoding="utf=8") as arquivo:
    for lin in arquivo:
        lin = lin.replace(",", "").replace("!", "")
        palavras += lin.upper().split()
print(palavras)

while True:
    palavra = input("Digite uma palavra que esteja no hino nacional: ")
    if palavra.upper() == 'SAIR':
        break
    elif palavra.upper() in palavras:
        print("Essa palavra está no hino!")
        print(f"Ela apareceu {palavras.count(palavra.upper())} no hino")
    else:
        print("Está palavra não está no hino!")
