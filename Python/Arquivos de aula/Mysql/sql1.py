import mysql.connector

conexão = mysql.connector.connect(user='root', password='naruto159', host ='127.0.0.1', database='agenda')

conexão.close()