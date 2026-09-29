#Write a Python program to check whether a list contains a sub list

l1 = [1, 2, 4, 6, 5, 2]

for i in l1:
    if type(i) == list:
        print("Yes")
