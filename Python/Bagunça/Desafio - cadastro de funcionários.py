<<<<<<< HEAD
dados_departamento = {
    1: 'RH',
    2: 'FINANÇAS',
    3: 'SAC',
    4: 'VENDAS',
    5: 'TI'
}

dados_funcionario = {
    100: dict(nome="José", admissao='01/05/2016', departamento=3),
    101: dict(nome="Maria", admissao='10/08/2018', departamento=1),
    102: dict(nome="Mariana", admissao='01/01/2019', departamento=4),
    103: dict(nome="Ana", admissao='01/05/2001', departamento=5),
    104: dict(nome="João", admissao='01/09/2014', departamento=1),
    105: dict(nome="Juca", admissao='01/07/2008', departamento=2)
}

def get_funcionario(codigo):
    if codigo in dados_funcionario:
        return dados_funcionario[codigo]
    else:
        print(f"O funcionario com código: {codigo}, não existe")
        return

def imprimir_funcionario(funcionario):
    for chave, valor in funcionario.items():
        if chave == 'departamento':
            print(f"{chave} : {dados_departamento[valor]}")
        else:
            print(f"{chave} : {valor}")

codigo = int(input("Digite o código do funcionário: "))
funcionario = get_funcionario(codigo)
if funcionario:
=======
dados_departamento = {
    1: 'RH',
    2: 'FINANÇAS',
    3: 'SAC',
    4: 'VENDAS',
    5: 'TI'
}

dados_funcionario = {
    100: dict(nome="José", admissao='01/05/2016', departamento=3),
    101: dict(nome="Maria", admissao='10/08/2018', departamento=1),
    102: dict(nome="Mariana", admissao='01/01/2019', departamento=4),
    103: dict(nome="Ana", admissao='01/05/2001', departamento=5),
    104: dict(nome="João", admissao='01/09/2014', departamento=1),
    105: dict(nome="Juca", admissao='01/07/2008', departamento=2)
}

def get_funcionario(codigo):
    if codigo in dados_funcionario:
        return dados_funcionario[codigo]
    else:
        print(f"O funcionario com código: {codigo}, não existe")
        return

def imprimir_funcionario(funcionario):
    for chave, valor in funcionario.items():
        if chave == 'departamento':
            print(f"{chave} : {dados_departamento[valor]}")
        else:
            print(f"{chave} : {valor}")

codigo = int(input("Digite o código do funcionário: "))
funcionario = get_funcionario(codigo)
if funcionario:
>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
    imprimir_funcionario(funcionario)