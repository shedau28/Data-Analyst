import pymysql
mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

while True:
    menu = '''
    Press 1 for Insert Data
    Press 2 for Update Data
    Press 3 for Delete Data
    Press 4 for Fetch Data
    Exit

'''

    print(menu)

    choice = int(input("Enter choice : "))

    if choice == 1:
        name = input("Enter name : ")
        mobile = input("Enter mobile number : ")

        query =  "insert into python80(name, mobile) values (%s, %s)"
        args = (name, mobile)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted")


    elif choice == 2:
        id = int(input("Enter ID : "))
        name = input("Enter name : ")
        mobile = input("Enter mobile number : ")

        query = "update python80 set name='%s', mobile='%s' where id='%s'" 
        args = (name, mobile, id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data is Updated")

    elif choice == 3:
        id = int(input("Enter ID : "))

        query = "delete from python80 where id = '%s'"
        args = (id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted")


    elif choice == 4:
        query = "select * from python80"
        mycursor.execute(query)

        data = mycursor.fetchall()
        print(data)