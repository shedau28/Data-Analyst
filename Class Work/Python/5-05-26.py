# l = []
# ev = []
# od = []


# for i in range(1, 31):
#     l.append(i)

#     if i%2==0:
#         ev.append(i)

#     else:
#         od.append(i)


# print(l)
# print(ev)
# print(od)

# l = [43, 92, 65, 11]

# l.sort()
# print("smallest Number : ", l[0])
# print("Largest Number : ", l[-1])
# print("Second Largest Number : ", l[-2])

# l = [16, 62, 24, 62, 16, 31]
# uniq = []
# for i in l:
#     if i in uniq:
#         pass
#     else:
#         uniq.append(i)
        
    
# print(uniq)


l = [16, 62, 24, 62, 16, 31]
n = int(input("Enter number : "))
count = 0
for i in l:
    if i == n:
        count += 1

print(count)


