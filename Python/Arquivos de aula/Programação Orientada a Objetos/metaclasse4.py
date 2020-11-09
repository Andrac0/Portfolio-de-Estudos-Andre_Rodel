def fabrica_de_funcoes(nome_metodo, retorno):
    def metodo_criado(self):
        return retorno

    metodo_criado.__name__ = nome_metodo
    return metodo_criado

class MinhaMetaClasse(type):
    def __new__(mcs, name, bases, attrib):
        for name, retorno in (('metodo1', 'Olá'), ('metodo2', str(70 + 7))):
            attrib[name] = fabrica_de_funcoes(name, retorno)

        return super().__new__(mcs, name, bases, attrib)
        
class MinhaClasse(metaclass=MinhaMetaClasse):
    pass

print("vars(MinhaClasse):", vars(MinhaMetaClasse))

mc = MinhaClasse()

print(mc.metodo1())
print(mc.metodo2())
