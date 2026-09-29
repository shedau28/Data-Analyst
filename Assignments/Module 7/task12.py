#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))

if n1 == n2 or n1 == n3 or n2 == n3:
    result = 0
    print("result is : ", result)
else:
    result = n1 + n2 + n3
    print("result is : ", result)
    