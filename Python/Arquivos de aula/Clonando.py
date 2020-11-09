lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_copia = lista_numeros #Assim teremos uma cópia exata, ou seja, tudo que tiver em uma terá na outra
print(lista_numeros)
print(lista_copia)
lista_numeros += [11]
print(lista_numeros)
print(lista_copia)
lista_copia += [12]
print(lista_numeros)
print(lista_copia)

lista_clone = lista_numeros[:] #Deste modo será um clone total da "lista_numeros", e para isso deve-se utilizar o método de "fátias"
print(lista_numeros)
print(lista_clone)
lista_numeros += [13]
print(lista_numeros)
print(lista_clone)
lista_clone += [14]
print(lista_numeros)
print(lista_clone)

lista_clone2 = lista_numeros[2:7:2]
print(lista_numeros)
print(lista_clone2)

lista_numeros[2:5] = [77,88,99]
print(lista_numeros)
lista_numeros[2:5] = []
print(lista_numeros)