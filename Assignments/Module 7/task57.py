#Write a Python program to find the highest 3 values in a dictionary

d = {'a': 200, 'b': 100, 'd': 400, 'c': 300}

val = sorted(d.values())
print(val[:3])
