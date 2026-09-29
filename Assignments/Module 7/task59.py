#Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.


text = 'hello world'
data = {}

for i in text:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(data)