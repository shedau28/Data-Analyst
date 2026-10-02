#  Write a Python program to read an entire text file.

file = open("test1.txt", 'w')
file.write("Test File Only")
file.close()

file = open("test1.txt", 'r')
file.seek(0)
print(file.read())
file.close()

