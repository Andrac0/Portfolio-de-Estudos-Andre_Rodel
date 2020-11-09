import mysql.connector

conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
cursor = conexao.cursor()

atualizar_contato = ("update contatos set nome = %s, telefone = %s, celular = %s where id = 1")

contato = ('Pocahontas','(92)1238-7854','(92)29546-9875')

cursor.execute(atualizar_contato, contato)
conexao.commit()
cursor.close()
conexao.close()