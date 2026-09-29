#  Write a Python program to read last n lines of a file. 
n = int(input("Enter number of last lines : "))
file = open("test1.txt", 'r')
lines = file.readlines()[-n:]
for i in lines:
    print(i)
file.close()