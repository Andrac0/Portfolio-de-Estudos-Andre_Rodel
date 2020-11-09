class Carro(object):
    marca = "Ford"
    __modelo = "Focus"
    _rodas = "Leves"

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

carro = Carro()
print(carro.marca)
carro.marca = "Fiat"
print(carro.marca)
carro.set_modelo("Uno")
print(carro.get_modelo())
carro._Carro__modelo = "Pálio"
print(carro.get_modelo())

print(carro._rodas) #Os atributos com somente 1 "#" indicam ser "não públicos", ou seja não
#é recomendado acessa-los diretamente e sim se disponivel por seus atribudos "get" e "set".

#print(carro.__modelo)

#Não funcionam devido ao fato de que o objeto "__modelo" é uma classe privada.

#print(carro.modelo)