class MinhaString(str):
    def __sub__(self, other):
        print("self:", self)
        print("other:", other)
        subtracao = self.replace(other, '')
        #subtracao = self.replace(other, 'legal')   Também é possível
        return f"Resultado de '{self}' - '{other}': {subtracao}"

s1 = MinhaString("Olá mundo cruel")
s2 = "cruel"

s3 = s1 - s2
print(s3)