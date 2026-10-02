#Write a Python script to check if a given key already exists in a dictionary. 

d1 = {1: 'h', 2: 'b', 3: 'c', 4: 'a', 5: 'c', 6: 'd'}
k1 = int(input("Enter key : "))

if k1 in d1.keys():
    print("Key Exists")
else:
    print("Not Exists")

