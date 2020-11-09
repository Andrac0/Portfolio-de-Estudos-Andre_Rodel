valor_da_parcela = float(input("Digite o valor da parcela: "))
meses = int(input("Digite a quantidade de meses que ira pagar por este produto: "))
valor_do_produto = valor_da_parcela * meses
print(f"O valor do seu produto é:R${valor_do_produto:,.2f}")

