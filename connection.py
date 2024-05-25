import mysql.connector
connection = mysql.connector.connect(host = "localhost", user = "root", password = "absolute.444", database = "Chess")
cursor = connection.cursor(dictionary = True)