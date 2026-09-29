#  Write a Python program to count the number of lines in a text file. 

file = open("test1.txt", 'r')
lines = file.readlines()
print(len(lines))
file.close()