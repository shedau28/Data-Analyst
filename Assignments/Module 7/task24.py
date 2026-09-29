#Write a Python function to insert a string in the middle of a string. 

n1 = input("Enter string : ")
n2 = input("Enter string : ")

mid = len(n1)//2

print(n1[:mid] + n2 + n1[mid:])