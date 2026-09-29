#  Write a python program to find the longest words.

size = 0
word = ""
file = open("test1.txt", 'r')

for line in file:
    # print(line)
    lines = line.strip()
    lines = lines.lower()
    words = lines.split(" ")
    # print(words)

    for i in words:
        check = len(i)

        if check > size:
            size = check
            word =  i   
    
print(word)