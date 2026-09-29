"""l1=[1,2,3,4,5,6]

l2=l1   # shallow copy  
l1.append(77)

print(l1)   # 1,2,3,4,5,6,77
print(l2)  # 1,2,3,4,5,6

l1=[1,2,3,4,5,6]
l2=l1.copy()   # deep  copy  
l1.append(77)

print(l1)  # 1 2 3 4 5 6,77
print(l2)  # 1 2 3 4 5 6 ,77 
"""

# pip install numpy  

import numpy as np

"""
arr =np.array([1,2,3,4,5,6])
print(arr)  # access index    =----> start index 0 
"""
# array attributes :

"""arr =np.array([1,2,30,4,5,60])

print(arr)
print(arr.shape)  # number  of rows and  columns
print(arr.ndim)  # number of dimensions
print(arr.dtype)  # data type  
print(arr.size)  # number of elements
print(arr.itemsize)  # size of each element
"""


# arr2 =np.array(
#     [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# )



# print(arr2)
# print(arr2.shape)
# print(arr2.ndim)
# print(arr2.dtype)
# print(arr2.size)
# print(arr2.itemsize)



arr =np.array(
    [[1,12,3],
     [4,5,6],
     [7,8,9]]
)

# 2d array  : 

"""
arr =np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)
print(arr)
print(arr.shape)  # number  of rows and  columns
print(arr.ndim)  # number of dimensions
print(arr.dtype)  # data type
print(arr.size)  # number of elements
"""

# 3d array : 

"""arr =np.array(
    [[[1,2,3],
     [4,5,6],
     [7,8,9]]]
)
print(arr.ndim)
"""


# arr = np.array([10, 20, 30, 40, 50])
# Change 10 to 100.
# arr[0] = 100
# Change 30 to 300.
# arr[2] = 300

# Change the last element 50 to 500.
# arr[-1] = 500
# Change the first two elements to 1 and 2.
# Change all elements greater than 30 to 0.
# Add 10 to every element.
# arr[:] = arr + 10
# Multiply every element by 2.
# arr[:] = arr * 2
# Change the middle element to 999.
# Change elements at indexes 1 and 3 to 0.
# arr[1:4:2] = 0
# Replace every even number with -1.
# arr[1: :2] = -1

# print(arr)


# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# Change 10 to 100.
# arr[0,0] = 100
# Change 50 to 500.
# arr[1,1] = 500
# Change 90 to 900.
# arr[2,2] = 900
# Change the entire first row to [1, 2, 3].
# arr[0, :] = [1,2,3]
# Change the entire second column to [0, 0, 0].
# arr[:, 1] = [0, 0, 0]
# Add 10 to every element.
# arr[:, :] = arr + 10
# Multiply the third row by 2.
# arr[2, :] = arr[2, :]*2
# Change all elements greater than 50 to -1.
# arr[arr > 50] = -1
# Change the diagonal elements to 0.
# Swap the first and third rows.



# arr = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# Change 1 to 100.
# arr[0, 0, 0] = 100
# Change 6 to 600.
# arr[0,1,2] = 600
# Change 12 to 1200.
# arr[1,1,2] = 1200
# Change the first 2D array to all zeros.
# arr[0, : , : ] = 0
# Change the second row of the first 2D array to [10, 20, 30].
# arr[0, 1, :] = [10, 20, 30]
# Add 5 to every element.
# arr[ : , : , : ] = arr[ : , : , : ] + 5
# Multiply the second 2D array by 2.
# Change all elements greater than 8 to 0.
# arr[arr > 8] = 0
# Change the element at index [1, 0, 2] to 999.
# arr[1, 0, 2] = 999
# Change every 2nd element along the last dimension to -1.


# print(arr)

# update  :

# arr =np.array([10,20,30,40,50,60])             
# arr[4]=999  # update 
# print(arr)

"""arr =np.array(
    [[1,2,3,56],   #row  1  ----> 0
     [4,5,6,54],  # row 2   ----> 1
     [7,8,9,34]]   # row 3   ----> 2
)
# arr[1,2] =888  # 1 ----> row index   2 ----> column index
# arr[1:3,1:2] =777  # row 1 start index   3 endindex 
arr[0:2 , 2] =88  # row 1 start index   3 endindex 

print(arr)
"""
# method  : np.arange , np.zero,np.ones ,np.full
"""arr =np.arange(1,10)  # last number excluded 
arr =np.arange(1,10,2)  # start 1  end 10  step 2 
arr =np.arange(1,10,4)

arr =np.arange(1,11).reshape(5,2)  # first arg  is row  and second is column
print(arr)
"""

# np.zeros 

"""arr =np.zeros(5,dtype=int)  # 5 zeros
arr =np.zeros((5,2),dtype=int)  # 5 zeros
print(arr)
"""

# np.ones :
"""arr=np.ones(5)  # 5 ones
arr=np.ones((3,3),dtype=int)  # 3 3 ones
print(arr)
"""

# np.full :

arr = np.full((4,3),fill_value=100,dtype=int)  # 4 3 999
# print(arr)

# HW : 
"""
1.Create an array of 10 student marks using np.array().
2.Generate even numbers from 2 to 50 using np.arange().
3.Create 8 equally spaced values from 100 to 500 using np.linspace().
4.Create a 4*4 matrix of zeros.
5.Create a 5*5 identity matrix.
6.Generate 20 random marks between 35 and 100.
7.Select 3 random fruits using np.random.choice().
8.Use np.random.seed(50) and generate 10 random integers between 1 and 100. Compare the output by running the code twice.

 ----> 1,2 4 

"""

'''1.Create an array of 10 student marks using np.array().'''
arr = np.array([
    [78, 85, 92, 74],
    [65, 72, 81, 69],
    [91, 88, 95, 90],
    [56, 64, 73, 61],
    [82, 79, 87, 85],
    [74, 68, 76, 80],
    [95, 93, 89, 97],
    [61, 75, 68, 72],
    [88, 84, 91, 86],
    [70, 62, 79, 66]
])
print(arr)

'''2.Generate even numbers from 2 to 50 using np.arange().'''
arr2 = np.arange(2,50,2)
print(arr2)

'''4.Create a 4*4 matrix of zeros.'''

arr3 = np.zeros((4,4))
print(arr3)


# 3.Create 8 equally spaced values from 100 to 500 using np.linspace().
arr4 = np.linspace(100,500,8)
print(arr4)


# 5.Create a 5*5 identity matrix.
arr5 = np.identity(5)
print(arr5)

import random as r
# 6.Generate 20 random marks between 35 and 100.
arr6 = np.random.randint(35,100,20)
print(arr6)

# 7.Select 3 random fruits using np.random.choice().
print(np.random.choice(['Apple', 'Orange', 'Guava', 'Banana', 'Lemon']), )
