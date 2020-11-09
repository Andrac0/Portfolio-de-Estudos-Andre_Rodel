
class Descritor_Valor(object):
    def __init__(self):
        self.valor = {}

    def __get__(self, instance, owner):
        return self.valor[instance]

    def __set__(self, instance, value):
        if value<0:
            raise ValueError("O valor do carro não pode ser negativo.")
        else:
            self.valor[instance] = value
    def __delete__(self, instance):
        del self.valor[instance]

class Carro(object):
    valor = Descritor_Valor()
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        #if valor<0:
        #    raise ValueError("O valor do carro não pode ser negativo.")
        #else:
        #    self.valor = valor
        self.valor = valor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Valor: R$ {self.valor:.2f}"

fusquinha = Carro("VW", "Fusca", 8500)
gol = Carro("VW", "Gol", 25000)
print(fusquinha)
print(gol)
print(fusquinha)