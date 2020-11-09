itens = ["Carne Bovina", "Frango", "Salsicha", "Peixe", "Carne Suína"]
for indice, carnes in enumerate(itens, start=1): #Pode ser tanto vazio quanto utilizando o "start", ou seja: emumerate(itens, 1)
    print(indice, carnes)

itens.sort()
for indice, carnes in enumerate(itens):
    print(indice+1, carnes)