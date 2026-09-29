import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="root")
mycur = mydb.cursor()
mycur.execute("create database if not exists python001")
mydb.commit()

mydb = pymysql.connect(host="localhost", user="root", password="root", database="python001")
mycur = mydb.cursor()
mycur.execute("create table if not exists programminglang (id int primary key auto_increment, name varchar(56), price int, duration int)")
mydb.commit()

