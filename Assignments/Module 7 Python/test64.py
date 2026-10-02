# Write a Python function that checks whether a passed string is palindrome or not 


def check_pal(text):
    new_text = text[::-1]

    if text == new_text:
        print("Entered string is pallindrom")
    else:
        print("Not a palindrome")


text = input("Enter a word : ")
check_pal(text)