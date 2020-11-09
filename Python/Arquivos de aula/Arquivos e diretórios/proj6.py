with open("Arquivos e diretórios/arquivo teste dois.txt", "a") as arquivo:
    arquivo.write("Linha adicionada\n")


with open("Arquivos e diretórios/arquivo teste dois.txt") as arquivo:
    for linha in arquivo:
        print(linha)