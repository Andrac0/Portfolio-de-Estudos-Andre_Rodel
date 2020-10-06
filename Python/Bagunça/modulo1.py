<<<<<<< HEAD
def soma(*valores):
    total = 0
    for numero in valores:
        total += numero
    return total

def media(*valores):
    total = soma(*valores)
    return total/len(valores)

=======
def soma(*valores):
    total = 0
    for numero in valores:
        total += numero
    return total

def media(*valores):
    total = soma(*valores)
    return total/len(valores)

>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
print(f"Média: {media(10, 8, 9.5)}")