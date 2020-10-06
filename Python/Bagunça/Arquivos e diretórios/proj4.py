arq = open("Arquivos e diretórios/teste_aula.txt", "r")

for lin in arq.readlines():
    print(lin)
arq.close()