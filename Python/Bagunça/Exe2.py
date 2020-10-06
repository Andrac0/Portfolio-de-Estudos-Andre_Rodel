bancos1 = ["Banco do Brasil", "CEF", "Banestes"]
bancos1.append("Bradesco")
print(bancos1)

bancos2 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
bancos2.insert(3, "Sicred")
print(bancos2)

bancos3 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
bancos3.remove("CEF")
print(bancos3)

bancos4 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
bancos4.sort()
print(bancos4)

bancos5 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
bancos5.reverse()
print(bancos5)

bancos6 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
qtd_bradesco = bancos6.count("Bradesco")
print(f"A quantidade de ocorrências do banco Bradesco é: {qtd_bradesco}")

bancos7 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
bancos7.pop()
print(bancos7)

bancos8 = ["Banco do Brasil", "CEF", "Banestes", "Itaú", "Santander", 'Bradesco']
print(bancos8)
del bancos8[3]
print(bancos8)
del bancos8[1:3]
print(bancos8)
