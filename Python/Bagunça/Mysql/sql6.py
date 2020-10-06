import mysql.connector

conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')

cursor = conexao.cursor()

inserir_contato = ("insert into contatos (nome, telefone, celular) "
                    "valuer ('Pateta', '(27)11111-1111', '(27)12345-3333')")

cursor.execute(inserir_contato)

conexao.commit()

cursor.close()

conexao.close()