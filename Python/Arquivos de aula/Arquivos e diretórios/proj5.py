arq = open("Arquivos e diretórios/teste2.txt", "w")

lista = ["Laranja\n", "Maça\n", "Abacaxi\n", "Amora\n", "Melancia\n"]

arq.writelines(lista)
arq.close()