#Write a Python function to get the largest number, smallest num and sum of all from a list. 

def largest_number(l1):
    l2 = sorted(l1)
    print("Largest number : ", l2[-1])

def smallest_number(l1):
    l2 = sorted(l1)
    print("Smallest number : ", l2[0])

def sum(l1):
    res = 0
    for i in l1:
        res += i
    print("Sum is : ", res)


x = [23, 43, 66, 1, 34, 65]
largest_number(x)
smallest_number(x)
sum(x)