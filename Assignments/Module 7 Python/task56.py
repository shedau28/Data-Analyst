#Write a Python program to map two lists into a dictionary Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 


l1 = ['a', 'b', 'd', 'c']
l2 = [400, 400, 400, 300]
d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print(d)