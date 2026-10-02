#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 

l1 = []
for i in range(1, 30):
    l1.append(i*i)

print(l1)

print("First 5 elements : ", l1[:5])

print("Last 5 elements : " ,l1[-5:])