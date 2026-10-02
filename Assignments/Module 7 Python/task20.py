#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

n1 = input("Enter first string : ")
n2 = input("Enter second string : ")

n4 = n1[0:2] + n2[2:]
n3 = n2[0:2] + n1[2:]

new_str = n3 + " " + n4

print(new_str)