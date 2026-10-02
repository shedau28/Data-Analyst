#Write a Python script to concatenate following dictionaries to create a new one. 

d1 = {1 : 'a', 2 : 'b'}
d2 = {3 : 'c', 2 : 'b'}
d3 = {4 : 'a', 5 : 'c'}
d4 = {1 : 'h', 6 : 'd'}


d1.update(d2)
d1.update(d3)
d1.update(d4)
print(d1)