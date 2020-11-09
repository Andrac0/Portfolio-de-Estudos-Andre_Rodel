import mysql.connector

conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
cursor = conexao.cursor()

inserir_contato = ("insert into contatos (nome, telefone, celular) "
                    "valuer (%(nome_contato)s,%(telefone)s,%(celular)s)")

contato = {'nome_contato': 'Bela Adormecida',
            'telefone': '(98)1236-7854',
            'celular': '(98)23546-9875'}

cursor.execute(inserir_contato, contato)
conexao.commit()
cursor.close()
conexao.close()