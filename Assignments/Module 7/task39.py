#Write a Python program to find the second smallest number in a list

l1 = [1, 4, 2, 7, 5]

for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print("Second smallest number : ", l1[1])


