import numpy as np
import random
# 1. How to Creating a 3x3 Identity Matrix with Float Data Type? 

"""
arr1 = np.eye(3, dtype=float)
print(arr1)
"""

# 2. Create a 1D Array with Random Values between 0 and 1. 
"""
arr1 = np.random.random(size=10)
print(arr1)
"""
# 3. Create a 2D Array with Random Integer Values. 
"""
arr1 = np.random.randint(1,10,(2,2))
print(arr1)
"""
# 4. Creating an Array Using a Custom Function. 
"""
def custom_grid_func(i, j):
    return i * 10 + j

matrix = np.fromfunction(custom_grid_func, (3, 4), dtype=int)

print(matrix)
"""

# 5. Reshaping a 1D Array into a 2D Array 
"""
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

arr2 = arr1.reshape(2, 4)
print(arr2)
"""

# 6.How to Creating a 3x3 Array of Ones?
"""
arr1 = np.ones((3, 3), dtype=int)
print(arr1)
"""

# 7. How to get the common items between two pythons NumPy? 
""" 
Input:
a = np. array ([1,2,3,2,3,4,3,4,5,6]) 
b = np. array ([7,2,10,2,7,4,9,4,9,8]) 
Expected Output: 
array ([2, 4]) 
""" 
"""
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8]) 

c = np.intersect1d(a,b)
print(c)"""

# 8. From array a remove all items present in array b 
""" 
Input:
a = np. array ([1,2,3,4,5]) 
b = np. array ([5,6,7,8,9]) 
Expected Output: 
array ([1,2,3,4] 
"""
"""
a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9]) 

c = np.setdiff1d(a, b)
print(c)"""



# 9. Limit the number of items printed in python NumPy array a to a maximum of 6 elements.
""" 
Input
a = np. arrange (15) 
Expected Output: 
array ([ 0, 1, 2, ..., 12, 13, 14] 
"""
"""
np.set_printoptions(threshold=6)
a = np.arange(15)

print(a)
"""

# 10. Drop all nan values from a 1D NumPy array 
""" 
Input:
np. array ([1,2,3, np.nan,5,6,7, np.nan]) 
Desired Output: 
array ([ 1., 2., 3., 5., 6., 7.]) 
"""

arr = np.array([1,2,3, np.nan,5,6,7, np.nan]) 
