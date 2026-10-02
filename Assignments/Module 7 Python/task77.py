#  Write a Python program to read a file line by line store it into a variable.

file = open("test1.txt", 'r')
lines = file.readlines()[0:4]
print(lines)
file.close()