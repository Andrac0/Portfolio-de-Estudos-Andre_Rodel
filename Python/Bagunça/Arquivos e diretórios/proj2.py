arq = open("Arquivos e diretórios/teste_aula.txt", "r")

#print(arq.read()) Este irá ler todo o arquivo
print(arq.readline())
print(arq.readline())
print(arq.readline(5))
print(arq.readline())
arq.close()