salario_atual = float(input("Digite o seu salário atual: R$"))
percentual_aumento= float(input("Digite o percentual de aumento:"))
novo_salario = salario_atual+(salario_atual*(percentual_aumento/100))
print(f"O seu novo salário é: R${novo_salario:,.2f}")