#  Write a Python program to read a file line by line and store it into a list

file = open("test1.txt", 'r')
lines = file.readlines()[0:4]
print(lines)
file.close()