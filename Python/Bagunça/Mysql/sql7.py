import mysql.connector

conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
cursor = conexao.cursor()

inserir_contato = ("insert into contatos (nome, telefone, celular) "
                    "valuer (%s,%s,%s)")

contato = ('Rapunzel','(61)2525-5858','(61)98745-5555')

cursor.execute(inserir_contato)
conexao.commit()
cursor.close()
conexao.close()