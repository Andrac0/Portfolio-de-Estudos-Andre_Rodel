import mysql.connector

print(dir(mysql))
conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
cursor = conexao.cursor()

consulta = ("select nome, telefone, celular from contatos where nome like 'M%'")
cursor.execute(consulta)

for (nome, telefone, celular) in cursor:
    print(f"Nome: {nome}, telefone: {telefone}, celular: {celular}")

cursor.close()
conexao.close()