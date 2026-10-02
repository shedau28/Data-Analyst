# Write a Python program to get the Fibonacci series of given range. 

n = int(input("Enter range : "))

if n == 0:
    series = [0]
elif n == 1:
    series = [0]
elif n == 2:
    series = [0,1]
else:
    num1 = 0
    num2 = 1
    series = [0, 1]

    for i in range(2, n):
        sum = num1+num2
        num1 = num2
        num2 = sum
        series.append(num2)

print(series)

