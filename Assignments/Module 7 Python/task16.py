#Write a Python program to count the number of characters (character frequency) in a string .

n1 = input("Enter a string : ")
d = {}

for i in n1:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)