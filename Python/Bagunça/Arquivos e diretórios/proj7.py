with open("Arquivos e diretórios/hino nacional.txt", encoding="utf=8") as arquivo:
    for lin in arquivo:
        palavras = lin.split()
        print(palavras)