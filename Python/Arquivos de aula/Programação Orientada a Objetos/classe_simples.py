class Classe_simples():
    pass    ##significa que não tem nada, ou seja, só pra testar

print(type(Classe_simples))

teste = Classe_simples()
print(type(teste))

print(type(teste) == Classe_simples)

class Pessoa():
    especie = 'Humano'

print(Pessoa.especie)

Pessoa.vivo = True  #Adicionado dinamicamente
print(Pessoa.vivo)

homem = Pessoa()
print(homem.especie)
print(homem.vivo)

Pessoa.vivo = False
print(homem.vivo)       #Herdou da classe Pessoa

homem.nome = "André"
homem.sobrenome = "Lima"
print(homem.nome, homem.sobrenome)

def funcao_externa():
    b = 20
    a = 80
    print(f"Imprimindo 'b' em funcao_externa: {b}")
    print(f"Imprimindo 'a' em funcao_externa: {a}")
    def funcao_interna():
        c = 30
        b = 25
        a = 70
        print(f"Imprimindo 'c' em funcao_interna: {c}")
        print(f"Imprimindo 'b' em funcao_interna: {b}")
        print(f"Imprimindo 'a' em funcao_interna: {a}")

    funcao_interna()
    print(f"Imprimindo 'b' de novo em funcao_externa: {b}")

a = 10

print(f"Imprimindo 'a' no escopo global: {a}")
funcao_externa()
print(f"Imprimindo 'a' de novo no escopo global: {a}")

def funcao_externa():
    b = 20
    global a
    a = 80
    print(f"Imprimindo 'b' em funcao_externa: {b}")
    print(f"Imprimindo 'a' em funcao_externa: {a}")
    def funcao_interna():
        c = 30
        b = 25
        global a
        a = 70
        print(f"Imprimindo 'c' em funcao_interna: {c}")
        print(f"Imprimindo 'b' em funcao_interna: {b}")
        print(f"Imprimindo 'a' em funcao_interna: {a}")

    funcao_interna()
    print(f"Imprimindo 'b' de novo em funcao_externa: {b}")

a = 10

print(f"Imprimindo 'a' no escopo global: {a}")
funcao_externa()
print(f"Imprimindo 'a' de novo no escopo global: {a}")

class Ponto():
    x = 10
    y = 7

p = Ponto()

print(p.x) # 10 (do atributo da classe)
print(p.y) # 7 (do atributo da classe)
p.x = 12 # p obtÃ©m seu prÃ³prio atributo "x"
print(p.x) # 12 (encontrado na instÃ¢ncia)
print(Ponto.x) # 10 (O atributo da classe ainda Ã© o mesmo)
del p.x # Apagando o atributo da instÃ¢ncia
print(p.x) # 10 (Agoa que nÃ£o existe "x" na instÃ¢ncia, serÃ¡ retornado da classe)
p.z = 3
print(p.z) # 3
#print(Ponto.z) ### O objeto Ponto nÃ£o tem o atributo "z"
# AttributeError: type object 'Ponto' has no attribute 'z'