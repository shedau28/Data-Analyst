#Write a Python function that takes two lists and returns true if they have at least one common member. 

l1 = [1, 3, 6, 4]
l2 = [2, 0, 7, 9]

def check_list(l1, l2):
    count = 0
    for i in l1:
        if i in l2:
            count += 1
        else:
            count += 0

    if count > 0:
        return True
    else:
        return False

print(check_list(l1, l2))