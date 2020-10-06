<<<<<<< HEAD
def validar_itens(lista):
    soma_inteiros = 0
    qtd_inteiros = 0
    lista_str = []
    lista_list = []
    lista_dict = []
    for item in lista:
        if type(item) == int:
            soma_inteiros += item
            qtd_inteiros += 1
        elif type(item) == str:
            lista_str.append(item)
        elif type(item) == list:
            lista_list.append(item)
        elif type(item) == dict:
            lista_dict.append(item)
        else:
            print("Tipo nÃ£o reconhecido!")

    if soma_inteiros > 0:
        print(f"Foram encontrados {qtd_inteiros} inteiros. A soma dos nÃºmeros inteiros Ã©: {soma_inteiros}")

    if len(lista_str) > 0:
        print(f"Foram encontradas {len(lista_str)} strings. Veja as strings:")
        for i in lista_str:
            print(i)

    if len(lista_list) > 0:
        retorno = ""
        print(f"Foram encontradas {len(lista_list)} listas. Veja os itens das listas:")
        for lista in lista_list:
            for item in lista:
                retorno = retorno + str(item) + ", "
        print(retorno[0:-2])

    if len(lista_dict) > 0:
        print(f"Foram encontrados {len(lista_dict)} dicionÃ¡rios. Veja os itens:")
        for dic in lista_dict:
            print(f"Chaves: {dic.keys()}")
            print(f"Valores: {dic.values()}")

lista = [10, 43, 42, "Python", "OlÃ¡", [1,2,3], "Mundo", ["a","b","c"],
         {"Item 1":25, "Item 2": 65}, "Teste", {"key1":"Valor1","key2":"Valor2"}]

=======
def validar_itens(lista):
    soma_inteiros = 0
    qtd_inteiros = 0
    lista_str = []
    lista_list = []
    lista_dict = []
    for item in lista:
        if type(item) == int:
            soma_inteiros += item
            qtd_inteiros += 1
        elif type(item) == str:
            lista_str.append(item)
        elif type(item) == list:
            lista_list.append(item)
        elif type(item) == dict:
            lista_dict.append(item)
        else:
            print("Tipo nÃ£o reconhecido!")

    if soma_inteiros > 0:
        print(f"Foram encontrados {qtd_inteiros} inteiros. A soma dos nÃºmeros inteiros Ã©: {soma_inteiros}")

    if len(lista_str) > 0:
        print(f"Foram encontradas {len(lista_str)} strings. Veja as strings:")
        for i in lista_str:
            print(i)

    if len(lista_list) > 0:
        retorno = ""
        print(f"Foram encontradas {len(lista_list)} listas. Veja os itens das listas:")
        for lista in lista_list:
            for item in lista:
                retorno = retorno + str(item) + ", "
        print(retorno[0:-2])

    if len(lista_dict) > 0:
        print(f"Foram encontrados {len(lista_dict)} dicionÃ¡rios. Veja os itens:")
        for dic in lista_dict:
            print(f"Chaves: {dic.keys()}")
            print(f"Valores: {dic.values()}")

lista = [10, 43, 42, "Python", "OlÃ¡", [1,2,3], "Mundo", ["a","b","c"],
         {"Item 1":25, "Item 2": 65}, "Teste", {"key1":"Valor1","key2":"Valor2"}]

>>>>>>> 01320788e2260a11682f663b2dc5f44a321a699c
validar_itens(lista)