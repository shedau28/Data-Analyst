def addition():
    n1 = int(input("Enter first digit : "))
    n2 = int(input("Enter second digit : "))

    res = n1 + n2
    print("Result is : ",res)
def substraction():
    n1 = int(input("Enter first digit : "))
    n2 = int(input("Enter second digit : "))

    res = n1 - n2
    print("Result is : ",res)
def multiply():
    n1 = int(input("Enter first digit : "))
    n2 = int(input("Enter second digit : "))

    res = n1 * n2
    print("Result is : ",res)

notice = """
    Select 1 for Addition
    Select 2 for Substraction
    Select 3 for Multiplication
    Select 4 for Exit
"""


while True:
    print(notice)
    n = int(input("Enter Choice : "))

    if n == 1:
        addition()
    elif n == 2:
        substraction()
    elif n == 3:
        multiply()
    elif n == 4:
        print("Exit")
        break
    else:
        print("Invalid Input")
        break





# Function with parameter and arguments

def addition(n1, n2=0):   #Here n1 and n2 are parameters. But n2 is by default 0, which is default parameter. 
    print(n1+n2)

b1 = int(input())
b2 = int(input())
addition(b1, b2)

#Default parameter can be redefine if value is given when callin a function.
#If value is not define then it will take defaukt value by default.



def fun1():
    n1 = 2
    n2 = 3
    return n1+n2

print(fun1)


