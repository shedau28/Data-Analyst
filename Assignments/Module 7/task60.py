#Sample string:
#  'w3resource' Expected output:
# • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

text = 'w3resource'
data = {}

for i in text:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

print(data)