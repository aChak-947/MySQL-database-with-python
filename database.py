import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "@Temple123",
	#after the database has been created we add the following
	database = "testdb",
	)

my_cursor = mydb.cursor()

#CREATING A DATABASE
#my_cursor.execute("CREATE DATABASE testdb")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
# 	print(db)



#CREATING A TABLE IN A DATABASE
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
# 	print(table[0])



# # ADDING A SINGLE ENTRY TO THE DATABASE
# sql_stuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Avronil Chakraborty", "avronilchakraborty87@gmail.com", 22)
# my_cursor.execute(sql_stuff, record1)
# # To save the changes
# mydb.commit()    



# ADDING MULTIPLE ENTRIES TO THE TABLE