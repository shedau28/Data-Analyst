#  Write a Python program to count the frequency of words in a file. 

data = {}

file = open('test1.txt', 'r')

for line in file:
    # print(line)
    lines = line.strip()
    words = lines.lower()
    # print(words)
    word = words.split(" ")
    print(word)

    for i in word:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
file.close()
print(data)

