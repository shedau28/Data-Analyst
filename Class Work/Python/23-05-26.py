#File Management

# w - write - create new file
# r - read - read content
# a - append - append data in existing file
# w+ - write and read 
# r+ - read and write


# file = open("test.txt", 'w')
# file.write("Write Method")
# file.close()


# file = open("test.txt", 'a')
# file.write("\nAppend Method")
# file.close()


# file = open("test.txt", 'r')
# print(file.read())
# file.close()


# data = {1 : "SRH", 2 : "RCB", 3 : "GT", 4 : "KKR"}
# file = open("test.txt", 'a')
# file.write("\n")
# file.write(str(data))
# file.close()


# data = {1 : "SRH", 2 : "RCB", 3 : "GT", 4 : "KKR"}
# file = open("test.txt", 'a')
# for key, value in data.items():
#     file.write(f'\n {key} : {value}' )
# file.close()


# file = open("test.txt", "w+")
# file.write("Write method")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

file = open("test.txt", "r+")
print(file.read())
file.write("r+ method")
file.close()
