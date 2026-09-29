#  Write a Python program to write a list to a file.

l1 = ["hello", "Python", "programming", "high-level", "language", "engineering"]

file = open("test2.txt", "w+")
for i in l1:
    file.write(i)
    file.write("\n")

file.close()