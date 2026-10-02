# Write python program that user to enter only odd numbers, else will raise an exception. 

# n = int(input("Enter Odd Number : "))

try:
    n = int(input("Enter an odd number : "))
    
    if n%2 == 0:
        raise ValueError("You have entered an even number. FAILED!!!")
    print("PASS!!!")
except ValueError as e:
    print(e)
    print("Invalid Input")