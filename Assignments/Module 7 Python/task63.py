#Write a Python function to check whether a number is perfect or not.

def perfect_num(num):
    res = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            res += i

    if num == res:
        return True
    else:
        return False
    
print(perfect_num(28))