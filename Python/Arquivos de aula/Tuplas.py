a = (1,2,3,4,5,6)       #Tuplas são imutaveis
b = 7,9,
c = (8,)
d = 10
e = "Rodolfo", "Cleber", "Cleiton",\
    "Mario"     #A barra "\" sinaliza que a próxima linha é continuação
print(a,b,c,d)
print(b[0])
print(a[2:5])
print(e)
for nomes in e:
    print(nomes)

lista_e = list(e)
print(lista_e)

tupla_e = tuple(lista_e)
print(tupla_e)

nome1, nome2, *nome = e
print(f"{nome1}")
print(f"{nome2}")
print(f"{nome}")

*nome, nome1, nome2 = e
print(f"{nome1}")
print(f"{nome2}")
print(f"{nome}")