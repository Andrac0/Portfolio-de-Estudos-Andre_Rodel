import mysql.connector

config = {'user':'root', 'password':'naruto159',
'host':'127.0.0.1', 'database':'agenda'}

conexao = mysql.connector.connect(**config)
conexao.close()