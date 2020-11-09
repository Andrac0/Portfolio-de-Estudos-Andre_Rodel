from mysql.connector import connection

conexão = connection.MySQLConnection(user='root', password='naruto159', host ='127.0.0.1', database='agenda')

conexão.close()