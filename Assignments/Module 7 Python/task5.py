# Write a Python program to get the Factorial number of given numbers. 

n = int(input("Enter Number : "))
fac = 1
for i in range(1, n+1):
    fac = fac*i

print("Factorial is : " ,fac)
