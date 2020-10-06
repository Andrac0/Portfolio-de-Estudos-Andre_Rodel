<<<<<<< HEAD
def fatorial(x):
    if x <= 1:
        return 1
    else:
        return (x * fatorial(x-1))

n = int(input("Informe um número para encontrar o fatorial: "))

=======
def fatorial(x):
    if x <= 1:
        return 1
    else:
        return (x * fatorial(x-1))

n = int(input("Informe um número para encontrar o fatorial: "))

>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
print(f"O fatorial de {n} é {fatorial(n)}")