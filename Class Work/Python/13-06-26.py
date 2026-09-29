#Recursion

#Base Condition
#Recursive condition


# def fibo(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1
    
#     else:
#         # print(f"{n-1} + {n-2}")
        
#         return fibo(n-1) + fibo(n-2)
    
# for i in range(10):
#     print(fibo(i))
# print(fibo(10))


#Prime Number
def prime(n, div=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % div == 0:
        return False
    if div * div > n:
        return True
    else:
        return prime(n, div+1)
    
print(prime(7))



