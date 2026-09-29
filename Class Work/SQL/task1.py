from connections import *

mydb = pymysql.connect(host="localhost", user="root", password="root", database="python001")
mycur = mydb.cursor()

while True:
    note = '''
        Press 1 to add data
        Press 2 to update data
        Press 3 to delete data
        Press 4 to check data
        Press 5 to exit
        '''
    print(note)
    choice = int(input("Enter a choice = "))

    if choice == 1:
        name = input("Enter Name of language : ")
        price = int(input("Enter course price : "))
        duration = int(input("Enter duration in months : "))

        query = "insert into programminglang(name, price, duration) values('%s', '%s', '%s')"
        args = (name, price, duration)

        mycur.execute(query % args)
        mydb.commit()
        print("Data Added Successfully!")

    elif choice == 2:
        id = int(input("Enter id of data : "))
        updatenote = '''
        Press 1 for update all fields
        Press 2 for update name
        Press 3 for update price
        Press 4 for update duration
        '''
        print(updatenote)
        updch = int(input("Enter update choice : "))

        if updch == 1:
            name = input("Enter Name of language : ")
            price = int(input("Enter course price : "))
            duration = int(input("Enter duration in months : "))

            query = "update programminglang set name = '%s', price = '%s', duration = '%s' where id = '%s'"
            args = (name, price, duration, id)

            mycur.execute(query % args)
            mydb.commit()

            print("Data Updated Successfully!")

        elif updch == 2:
            name = input("Enter Name of language : ")
            
            query = "update programminglang set name = '%s' where id = '%s'"
            args = (name, id)

            mycur.execute(query % args)
            mydb.commit()
            print("Data Updated Successfully!")

        elif updch == 3:
            price = int(input("Enter course price : "))
            
            query = "update programminglang set price = '%s' where id = '%s'"
            args = (price, id)

            mycur.execute(query % args)
            mydb.commit()
            print("Data Updated Successfully!")
        
        elif updch == 4:
            duration = int(input("Enter duration in months : "))
            
            query = "update programminglang set duration = '%s' where id = '%s'"
            args = (duration, id)

            mycur.execute(query % args)
            mydb.commit()
            print("Data Updated Successfully!")

        else:
            print("Invalid Choice!")

    elif choice == 3:
        id = int(input("Enter id : "))

        delch = input("Are you sure you want to delete this? [y/n] : ")

        if delch == 'y':
            query = "delete from programminglang where id = '%s'"
            args = (id)

            mycur.execute(query % args)
            mydb.commit()
            print("Data Deleted!")
        else:
            print("Data not deleted")
            
    elif choice == 4:
        checknote = ''' 
        Press 1 to search specific data
        Press 2 to check all data
        '''
        print(checknote)
        checkch = int(input("Enter choice : "))
        if checkch == 1:
            id = int(input("Enter id : "))
            
            query = "select * from programminglang where id = '%s'"
            args = (id)

            mycur.execute(query % args)
            data = mycur.fetchone()
            print(data)
        
        else:
            query = "select * from programminglang"
            mycur.execute(query)
            data = mycur.fetchall()
            print(data)

    elif choice == 5: 
        break

    else:
        print("Invalid Choice!")