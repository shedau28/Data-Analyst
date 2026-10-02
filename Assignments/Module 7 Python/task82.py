#  Write a Python program to copy the contents of a file to another file. 


file = open("test2.txt", 'r')
content = file.readlines()
file2 = open("test3.txt", 'w')
for i in content:
    file2.write(i)

file2.close()
file.close()