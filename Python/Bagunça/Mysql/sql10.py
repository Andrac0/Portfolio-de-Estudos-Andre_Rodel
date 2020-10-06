import mysql.connector

conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
cursor = conexao.cursor()

remover_contato = ("delete from contatos where id = 1")

cursor.execute(remover_contato)
conexao.commit()
cursor.close()
conexao.close()