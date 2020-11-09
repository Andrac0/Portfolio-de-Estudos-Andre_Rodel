valor = input("Informe um número: ")

try:
    soma = int(valor) + 10
    resultado = soma / int(valor)

#except:
#    print("Deu ruim")

#except ZeroDivisionError:
except ZeroDivisionError as erro:
    print("Opa, ocorreu um erro de divisão por zero!", erro)
    
#except ValueError:
except ValueError as e:
    print("Opa, ocorreu um erro de valor!", e)

else:
    print("Legal, não deu nenhum erro!")

finally:
    print("Isso sempre é executado")

#Sempre seguirá o curso, mesmo com erro, mas somente quando há exeções sendo aplicadas
x = 10
y = 25
print("X + Y =", x+y)