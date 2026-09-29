# #EXCEPTION HANDELING

# try:
#     n = int(input("Enter a number : "))
#     res = 10%n
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("Try Exwcuted")
# finally:
#     print("Finally")




# try:
#     n = int(input("Enter a number : "))
#     res = 10%n
# except Exception as e:
#     print()
#     print("Invalid Input")



import random
otp = random.randint(1001, 9999)

data = {}

while True:

    note = '''
    Choose 1 for signup
    Choose 2 for Login
    Choose 3 for Forget Password
    Choose 4 for Exit
    '''

    print(note)

    try:
        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter name : ")
            email = input("Enter email : ")
            mob = input("Enter mobile no. : ")
            password = int(input("Enter password : "))
            cpassword = int(input("Enter password again : "))

            if password == cpassword:
                data['name'] = name
                data['email'] = email
                data['mob'] = mob
                data['password'] = password
                
            else:
                print("Passwords does not match:")


        elif choice == 2:
            email = input("Enter email : ")
            password = int(input("Enter password : "))

            if data['email'] == email and data['password'] == password:
                print("Login successful")
            else:
                print("Credentials does not match")

        elif choice == 3:
            mob = input("Enter mobile no. : ")
            if data['mob'] == mob:
                print("Your otp is : ", otp)

                uotp = int(input("Enter your otp : "))
                password = int(input("Enter password : "))
                cpassword = int(input("Enter password again : "))
                if otp == uotp:
                    if password == cpassword:
                        data['password'] == password
                        
                    else:
                        print("Passwords does not match:")
                else:
                    print("otp does not match")
            else:
                print("Mobile no not exists`")



        elif choice == 4:
            print("Thank you")
            break

        else:
            print("Please enter form 1 to 4")
    except:
        print("Invalid Input")



