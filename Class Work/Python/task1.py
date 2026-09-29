data = {}

class Book:
    def addBook(self):
        pass

class GetBook:
    pass

while True:

    note = """
        1. Add Book
        2. View Book
        3. Delete Book
        """
    print(note)

    choice = int(input("Enter choice : "))
    
    if choice == 1:
        id = int(input("Enter Book id : "))
        book_name = input("Enter Book Name : ")
        content = input("Enter Content : ")

        if id in data:
            print("Book Already Exists")
        else:

            data[id] = book_name 
            temp_book = f"{book_name}.txt"
            file = open(temp_book, 'w')
            file.write(content)
            file.close()       
        print(data)
    elif choice == 2:
        id = int(input("Enter Book id : "))

        if id in data:
            book_name = data[id]
            book = f"{book_name}.txt"
            file2 = open(book, 'r')
            file2.seek(0)
            
            print(file2.read())
            file2.close()
        print(data)
    elif choice == 3:
        id = int(input("Enter Book id : "))

        if id in data:
            data.pop(id)
            print("Successfully deleted")
            print(data)
        else:
            print("Book does not exists")
            print(data)

    else:
        print("Invalid Input")


