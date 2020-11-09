<<<<<<< HEAD
def validar_faixa(num, inicio, fim):
    if num.isdigit():
        if int(num) < int(inicio) or int(num) > int(fim):
            print(f"Valor Inválido! Informe um número entre {inicio} e {fim}.")
        else:
            return True
    else:
        print(f"Número inválido! Informe um número inteiro entre"
        f"{inicio} e {fim}.")

while True:
    resp = input("Informe um número entre 1 e 10: ")
    if validar_faixa(resp, 1, 10):
        break

def validar_tamanho(texto, max):
    if len(texto) > max:
        print(f"O texto deve conter no máximo {max} caracteres!")
    else:
        return True

while True:
    texto = input("Informe um texto de no máximo 20 caracteres: ")
    if validar_tamanho(texto, 20):
        break

def valida_elementos(texto, lista):
    if texto.upper() in lista:
        return True
    else:
        print("Opção inválida, veja as opções disponíveis:")
        for item in lista:
            print(item)

while True:
    lista = ["CARRO", "NAVIO", "ÔNIBUS", "AVIÃO"]
    resposta = input("Informe um meio de transporte: ")
    if valida_elementos(resposta, lista):
=======
def validar_faixa(num, inicio, fim):
    if num.isdigit():
        if int(num) < int(inicio) or int(num) > int(fim):
            print(f"Valor Inválido! Informe um número entre {inicio} e {fim}.")
        else:
            return True
    else:
        print(f"Número inválido! Informe um número inteiro entre"
        f"{inicio} e {fim}.")

while True:
    resp = input("Informe um número entre 1 e 10: ")
    if validar_faixa(resp, 1, 10):
        break

def validar_tamanho(texto, max):
    if len(texto) > max:
        print(f"O texto deve conter no máximo {max} caracteres!")
    else:
        return True

while True:
    texto = input("Informe um texto de no máximo 20 caracteres: ")
    if validar_tamanho(texto, 20):
        break

def valida_elementos(texto, lista):
    if texto.upper() in lista:
        return True
    else:
        print("Opção inválida, veja as opções disponíveis:")
        for item in lista:
            print(item)

while True:
    lista = ["CARRO", "NAVIO", "ÔNIBUS", "AVIÃO"]
    resposta = input("Informe um meio de transporte: ")
    if valida_elementos(resposta, lista):
>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
        break