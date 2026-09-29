# # Polymorphism

# # Method overloading - Not supported in python
# # Method Overriding - Same name but different characteristic

# class A:
#     def fun1(self):
#         super().fun1()
#         print("Method 1")

# class B:
#     def fun1(self):
#         print("Method 2")

# class C(A, B):
#     def fun1(self):
#         super().fun1()
#         print("Method 3")

# obj = C()
# obj.fun1()

# # Encapsulation

# # Pointer : stores the address of the variable or refrence variable

# class A:
    
#     def fun1(self):
#         a = 10
#         self.a = a #Here self.a is pointer which 

#     def fun2(self):
#         print(self.a)   #using pointer can access local variables

# obj = A()
# obj.fun1()
# obj.fun2()


import random


class Account():

    def acc_create(self):
        name = input("Enter your name : ")
        email = input("Enter email : ")
        mobile = int(input("Enter mobile number : "))
        wpass = input("Enter withdrawal password : ")
        acc_number = random.randint(1001, 9999)
        balance = 5000


        self.name = name
        self.email = email
        self.mobile = mobile
        self.acc_number = acc_number
        self.wpass = wpass
        self.balance = balance

        print("Account successfully created")
        print("Account Number : ",self.acc_number)


    def deposit(self):
        acc_num1 = int(input("Enter account number : "))
        if acc_num1 == self.acc_number:
            dep_amount1 = int(input("Enter deposit amount : "))
            self.balance += dep_amount1
            print("Balance = ", self.balance)
        else:
            print("Account number does not exists")
    
    def withdrawal(self):
        mob = int(input("Enter mobile no. : "))
        wpass1 = input("Enter withdrawal password : ")

        if mob == self.mobile and wpass1 == self.wpass:
            withdraw_amount = int(input("Enter amount to withdraw : "))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
            else:
                print("Poor")
        else:
            print("Incorrect credentials")

    def check_bal(self):
        acc_num = int(input("Enter account number : "))

        if acc_num == self.acc_number:
            print("Your balance is : ", self.balance)
        else:
            print("Wrong credentials")


obj = Account()

while True:
    note = '''
        Press 1 for create account
        Press 2 for Deposit
        Press 3 for Withdraw
        Press 4 for Check Balance
        '''

    print(note)
    choice = int(input("Enter choice : "))

    if choice == 1:
        obj.acc_create()

    elif choice == 2:
        obj.deposit()
    elif choice == 3:
        obj.withdrawal()
    elif choice == 4:
        obj.check_bal()
    else:
        break







