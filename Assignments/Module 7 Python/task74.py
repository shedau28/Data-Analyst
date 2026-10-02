#  Write a Python program to read first n lines of a file.

file = open("test1.txt", 'r')
lines = file.readlines()[0:4]
for i in lines:
    print(i)
file.close()