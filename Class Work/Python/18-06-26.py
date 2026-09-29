# lambda
# Synonum of function
# Single line function
# denote by lambda (Multiple args) : body of function


# x = lambda a, b, c : a + b + c
# print(x(4, 5, 6))

# y = lambda a : a * a
# print(y(5))



# CRUD OPERATIONS


import pymysql
# mydb = pymysql.connect(host="localhost", user="root", password="")
# mycursor = mydb.cursor()

# mycursor.execute("create database if not exists python67")
# mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists python80 (id int, primary_key int auto increment= ON, name varchar (28), mobile varchar (12))")
mydb.commit()


