nome = "André Lima"

print(nome.startswith("Naruto"))
print(nome.startswith("And"))

print(nome.endswith("Naruto"))
print(nome.endswith("ma"))

a = "Aula de Python"

print("teste" in a)

print("Aula" in a)
print("Python" in a)

print("Aula" not in a)

print("Teste" not in a)

print(a.lower())

print(a.upper())

print(a.upper().startswith("AULA"))
print(a.upper().startswith("Aula"))

print(a.lower().startswith("aula"))
print(a.upper().startswith("Aula"))