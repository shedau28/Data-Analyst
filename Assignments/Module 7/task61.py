#Write a Python function to calculate the factorial of a number (a nonnegative integer) 

num = int(input("Enter a number : "))
fac = 1
for i in range(1, num+1):
    fac = i*fac

print("Factorial is : ", fac)