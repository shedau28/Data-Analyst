#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 

def count_word(l1):
    cnt = 0
    for i in l1:
        if len(l1) >2 and i[0] == i[-1]:
            cnt += 1
    print(cnt)



count_word(["hello", "world", "pythonp", "helllloh", "isi", "am", "try", "again"]
)