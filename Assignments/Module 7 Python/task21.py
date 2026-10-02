#Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

# x > 3
# x + in
# xing + ly


n = input("Enter a string : ")

if len(n) > 3:
    if n[-3 : ] == 'ing':
        print(n + 'ly')
    else:
        print(n + "in")

else:
    print(n)