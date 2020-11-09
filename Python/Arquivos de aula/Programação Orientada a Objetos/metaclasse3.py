class MinhaMetaClasse(type):
    pass

#MinhaClasse = MinhaMetaClasse('MinhaClasse', (), {})
class MinhaClasse(metaclass=MinhaMetaClasse):
    pass

minhainstancia = MinhaClasse()
print(type(minhainstancia))