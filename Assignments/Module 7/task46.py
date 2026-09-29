#Write a Python program to convert a list of tuples into a dictionary. 

l1 = [(1, 2, 3), (4, 5, 6)]
data = {}

for i in range(len(l1)):
    data[i] = l1[i]

print(data)