#  Write a Python program to append text to a file and display the text. 

file = open("test1.txt", 'a')
file.write("\nAppending text here")
file.close()

file = open("test1.txt", 'r')
file.seek(0)
print(file.read())
file.close()
