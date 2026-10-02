#Write a Python program to remove duplicates from a list.

l1 = [1, 2, 3, 6, 3, 2, 8]

l2 = []

for i in l1:
    if i in l2:
        pass
    else:
        l2.append(i)

print(l2)