while True:
    abc = """
    1 for factorial number.
    2 for prime number.
    3 for reverse number.
    4 for exit.
    """
    print(abc)

    n = int(input("Enter Choice : "))
    

    if n==1:
        num = int(input("Enter Number : "))
        
        fac = 1
        for i in range(1, num+1):
            fac = fac * i
        print("Factorial of number is : ", fac)



    elif n==2:
        #Prime Number
        num = int(input("Enter Number : "))
        prime = 0

        for i in range(1, num+1):
            if num%i == 0:
                prime += 1

        if prime == 2:
            print("Prime Number")

        else:
            print("Not Prime Number")

    elif n==3:
        num = int(input("Enter Number : "))
        rem = 0
        rev = 0

        while num > 0:
            rem = num % 10
            rev = rev * 10 + rem
            num //= 10

        print(rev)  
        
        

    elif n==4:
        print("Exit")
        break
    else:
        print("Invalid Input")
        break