#Tuple and Type Conversion

# t1 = (1, 2, "hello", "welcome", True, 1.64)

# l1 = list(t1)
# print(l1)
# t2 = tuple(l1)
# print(t2)

#Tupple Methods
# print(t1.count(1))
# print(t1.index(2))



#Dictionary

d1 = {1:"Hellow", 2:"Hello", 3:"Hello"}
d3 = {5 : "Yess"}
# print(d1.get(1)) #get calue of specified key

# print(d1.keys()) 
# print(d1.values()) 
# print(d1.items()) #get all items means key & values

# print(d1.pop(2)) #removes specified key
# print(d1.popitem()) #removes last item from dict

# d1.update(d3) #Update with other dictionary
# print(d1)

# t1 = (5, 6, 7)
# d2 = {}
# print(d2.fromkeys(t1)) #we can specify value which will apply for all keys

d = {}
for i in range(1, 30):
    d[i] = i*i
print(d)

