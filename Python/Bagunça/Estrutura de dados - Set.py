conjunto_numeros = {10,30,40,10,42,42,56}
print(conjunto_numeros)

conjunto_frutas = {"Abacaxi","Abacaxi","Laranja","Maça","Abacaxi"}
conjunto_uniao = conjunto_frutas.union(conjunto_numeros)        #união de conjuntos
print(conjunto_uniao)

lista_numeros = [1,2,5,6,4,8,8,2]
conjunto_lista = set(lista_numeros)         #conversão de lista para conjunto em set
print(lista_numeros)
print(conjunto_lista)

conjunto_todos = {10,30,40,42,56,"Abacaxi", "Laranja", "Maçã"}
conjunto_diferenca = conjunto_todos.difference(conjunto_numeros)      #Mostra a diferença entre 
print(conjunto_diferenca)                                             #os dois conjuntos

conjunto_intersecao = conjunto_numeros.intersection(conjunto_todos) #Mostra o que tem em
print(conjunto_intersecao)                                          #comum

linguagemT = set()   #Conjunto vazio deve ser declarado assim

linguagens = {"Python", "Java", "C++"}
linguagem = {"Python"}
if linguagens.issuperset(linguagem):        #Verifica se incluí
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não inclui o conjunto linguagem.")
linguagem = {"Cobol"}
if linguagens.issuperset(linguagem):
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não inclui o conjunto linguagem.")


linguagem = {"Python"}
if linguagem.issubset(linguagens):  #Verifica se está incluso
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não inclui o conjunto linguagem.")
linguagem = {"Cobol"}
if linguagem.issubset(linguagens):
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não inclui o conjunto linguagem.")

linguagens1 = {"Python", "C++", "Assemnly"}
linguagens2 = {"Pascal", "Clipper", "Fortran"}
if linguagens1.isdisjoint(linguagens2):        #Verifica se não há elementos em comum
    print("Os conjuntos não possuem elementos em comum.")
else:
    print("Os conjuntos possuem elementos em comum.")
linguagens2 = {"Pascal", "Clipper", "Fortran", "Python"}
if linguagens1.isdisjoint(linguagens2):        
    print("Os conjuntos não possuem elementos em comum.")
else:
    print("Os conjuntos possuem elementos em comum.")