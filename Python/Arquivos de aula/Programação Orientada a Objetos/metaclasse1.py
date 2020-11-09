def meu_metodo(self):
    return 1

MinhaClasse = type('MinhaClasse', (object,), {'metodo': meu_metodo})

inst = MinhaClasse()
x = inst.metodo()
print(x)

#É o mesmo que:
#
#1  class MinhaClasse:
#2      def metodo(self):
#3          return 1
#4
#5  inst = MinhaClasse()
#6  x = inst.metodo()
#7  print(x)