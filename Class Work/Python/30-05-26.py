# Inheritance

# When One class derived the properties into another class it is called inheritance

# 1. Single Level
# 2. Multilevel
# 3. Multiple
# 4. Hierarchi
# 5. Hybrid 

# 1. Single
# class A:
#     def fun1(self):
#         print("Method 1!")

# class B(A):
#     def fun2(self):
#         print("Method 2!")

# obj = B()
# obj.fun1()
# obj.fun2()



# 2. Multilevel
# class A:
#     def fun1(self):
#         print("Method 1!")

# class B(A):
#     def fun2(self):
#         print("Method 2!")

# class C(B):
#     def fun3(self):
#         print("Method 3!")

# obj = C()
# obj.fun1()
# obj.fun2()
# obj.fun3()



# Name Roll Number Marks Grades


# data = {}


# class A:
#     def addStudent(self, name, roll):
#         print("Student Name : ", name)
#         print("Student Roll Number : ", roll)


# class B(A):
#     def marks(self, eng, maths, science):
#         total = eng + maths + science
#         print("Marks")
#         print("English : ", eng)
#         print("Maths : ", maths)
#         print("Science : ", science)
#         print("Total :", total)

#     def grade(self, eng, maths, science):
#         total = eng + maths + science
#         return total
    
# class C(B):
#     pass

# # class C(B):
# #     def grade(self):
        
# obj = C()
# obj.addStudent("Suyog", 12)
# obj.marks(87, 88, 76)
# avg = (obj.grade())/3



# 3. Multiple

# class A:
#     def fun1(self):
#         print("Method 1!")

# class B:
#     def fun2(self):
#         print("Method 2!")

# class C(A, B):
#     def fun3(self):
#         print("Method 3!")

# obj = C()
# obj.fun1()
# obj.fun2()
# obj.fun3()


# 4. Heirarchie

# Dont recommended because multiple objects need to create

# class A:
#     def fun1(self):
#         print("Method 1!")

# class B(A):
#     def fun2(self):
#         print("Method 2!")

# class C(A):
#     def fun3(self):
#         print("Method 3!")

# obj1 = C()
# obj2 = B()

# obj1.fun1()
# obj1.fun3()
# obj2.fun1()
# obj2.fun2()


# 5. Hybrid

class A:
    def fun1(self):
        print("Method 1!")

class B(A):
    def fun2(self):
        print("Method 2!")

class C():
    def fun3(self):
        print("Method 3!")

class D(B, C):
    def fun4(self):
        print("Method 4!")

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()