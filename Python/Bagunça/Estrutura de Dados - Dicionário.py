<<<<<<< HEAD
carros = {'marca' : 'VW', 'modelo': 'Gol', 'ano_modelo': 2016}

print(f'O ano do modelo do carro é: {carros["ano_modelo"]}')
print(f'A marca do carro é: {carros["marca"]}') 

carros['ano_fabricacao'] = 2017
print(f'O ano de fabricação do carro é: {carros["ano_fabricacao"]}')

del carros['modelo']
print(f"Removido modelo: {carros}")

dicionario = {'anime':'naruto','suco':'laranja','ano':2016}
dicionario.clear()  #Limpa o dicionário mas não o apaga
del dicionario      #Deleta o dicionário completamente

print(f"Itens do dicionário carros: {carros.items()}")
print(f"chaves do dicionário carros: {carros.keys()}")
print(f"Valores do dicionário carros: {carros.values()}")

"marca" in carros           #Verificar se existe essa chave no dicionário carros

carros2 = carros.copy()
print(carros2)

carros['melhor_ano'] = 2020
carros2.update(carros)
print(carros2)

=======
carros = {'marca' : 'VW', 'modelo': 'Gol', 'ano_modelo': 2016}

print(f'O ano do modelo do carro é: {carros["ano_modelo"]}')
print(f'A marca do carro é: {carros["marca"]}') 

carros['ano_fabricacao'] = 2017
print(f'O ano de fabricação do carro é: {carros["ano_fabricacao"]}')

del carros['modelo']
print(f"Removido modelo: {carros}")

dicionario = {'anime':'naruto','suco':'laranja','ano':2016}
dicionario.clear()  #Limpa o dicionário mas não o apaga
del dicionario      #Deleta o dicionário completamente

print(f"Itens do dicionário carros: {carros.items()}")
print(f"chaves do dicionário carros: {carros.keys()}")
print(f"Valores do dicionário carros: {carros.values()}")

"marca" in carros           #Verificar se existe essa chave no dicionário carros

carros2 = carros.copy()
print(carros2)

carros['melhor_ano'] = 2020
carros2.update(carros)
print(carros2)

>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
print(len(carros2))