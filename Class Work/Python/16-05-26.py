n = int(input("Enter a range : "))

l1 = []
sum = 0

if n > 0:
    for i in range(1, n):
        sum += i
        l1.append(sum)
        print(l1)

print(l1)