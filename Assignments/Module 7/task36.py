#Write a Python function that takes a list and returns a new list with unique elements of the first list. 

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