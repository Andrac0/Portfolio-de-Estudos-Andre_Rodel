import mysql.connector
from mysql.connector import errorcode

try:
    conexao = mysql.connector.connect(user='root',password='naruto159',host='127.0.0.1',database='agenda')
except mysql.connector.Error as erro:
    if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha inválidos")
    elif erro.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(erro)
else:
    conexao.close()