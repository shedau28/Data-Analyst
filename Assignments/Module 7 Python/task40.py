#Write a Python program to get unique values from a list 


def unique_list(l1):
    l2 = []
    for i in l1:
        if i in l2:
            pass
        else:
            l2.append(i)

    return l2

check = unique_list([1, 2, 3, 4, 4, 5, 1, 6])
print(check)