# palindrome
# s = input("Enter Name :")
# if s==s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# find middle 3 chars

# s = input("Enter Name :")

# if len(s)%2==0:
#     print("This is even character string")
# else:
#     mid = len(s)//2
#     print(s[mid-1:mid+2:1])
#     # or
#     print(s[mid-1]+s[mid]+s[mid+1])





# "LIST"

l1 = [1,3,5,"hello", True, 9,22]

print(type(l1))

l1.append(6)  #arg=value you want to append
print(l1)

print(l1.count(1))   #arg=value to find its count

# l1.extend(l2) args=other list to append it whole 

print(l1.index(9))  #arg=value to find its first occurance in list

l1.pop()  #removes last value in list

l1.remove(5)  #arg=value to remove from first occured index
print(l1)

