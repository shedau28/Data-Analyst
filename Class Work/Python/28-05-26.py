# # OOPS : Object oriented programming system.

# # Pillars of OOPS
# # 1. Class - object
# # 2. Inheritance
# # 3. Polymorphism
# # 4. Encapsulation
# # 5. Abstraction



# class MyClass():

#     def addition(self, a , b):
#         res = a + b
#         return res
#     def substraction(self, a , b):
#         res = a - b
#         return res
#     def multiplication(self, a , b):
#         res = a*b
#         return res
#     def division(self, a , b):
#         res = a/b
#         return res

# while True:
#     note = """
#         ===Calculator===
#         Press 1 for Addition.
#         Press 2 for Substraction.
#         Press 3 for Multiplication.
#         Press 4 for Division.
#     """
#     obj = MyClass()
#     try:
#         choice = int(input("Enter your choice : "))
        
#         if choice == 1:
#             n1 = int(input("Enter first number : "))
#             n2 = int(input("Enter second number : "))

#             ans = obj.addition(n1, n2)
#             print("Answer is : ", ans)

#         elif choice == 2:
#             n1 = int(input("Enter first number : "))
#             n2 = int(input("Enter second number : "))

#             ans = obj.substraction(n1, n2)
#             print("Answer is : ", ans)

#         elif choice == 3:
#             n1 = int(input("Enter first number : "))
#             n2 = int(input("Enter second number : "))

#             ans = obj.multiplication(n1, n2)
#             print("Answer is : ", ans)
#         elif choice == 4:
#             n1 = int(input("Enter first number : "))
#             n2 = int(input("Enter second number : "))
#             if n1 <= 0 or n2 <= 0 :
#                 print("Enter positive number")
#             else:
#                 ans = obj.division(n1, n2)
#                 print("Answer is : ", ans)

#         else:
#             print("Invalid Choice")
#     except:
#         print("Please Enter A Number")




class MyClass3():
    def fun3(self):
        print("Class 3....")
class MyClass2():
    def fun2(self):
        print("Class 2....")
class MyClass1():
    def fun1(self):
        print("Class 1 ...")    

obj1 = MyClass1()
obj2 = MyClass2()
obj3 = MyClass3()
