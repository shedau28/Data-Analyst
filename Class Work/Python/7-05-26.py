#Complexity

#Time Complexity
    #Time needed to execution

#Space Complexity
    #Space needed

# Best Case == Alpha
# Avg Case == Omega
# Worst Case == Big Notation 0

# 0(1) >>> 1 to 10
# 0(2) >>> 1 to 10 and 11 to 12



# l = [1, 2, 3, 23, 1]

# left = 0
# right = len(l)-1
# ans = "yes"

# while (left < right):
#     if l[left] == l[right]:
#         left += 1
#         right -= 1
#     else:
#         ans = "no"
#         break

# print(ans)

# reverse 

# l = [10, 43, 22, 55, 9,44]

# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         l[i], l[j] = l[j], l[i]

# print(l)

#Best Case

# left = 0
# right = len(l)-1

# while (left < right):
#     l[left],l[right] = l[right], l[left]
#     left += 1
#     right -= 1

# print(l)





#Sorting

#Bubble Sort


#Ascending Order
# l = [10, 43, 22, 55, 9,44]

# for i in range(0, len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]

# print(l)


#descending Order
l = [10, 43, 22, 55, 9,44]

for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

print(l)



#Merge Sort


