arq = open("Arquivos e diretórios/teste_aula.txt", "r")

#print(arq.readlines())

linhas = arq.readlines()

print(linhas[3])
arq.close()