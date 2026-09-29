import numpy as np

"""
Find the Maximum Element in a Numpy Array

Input: arr = np.array([1, 3, 7, 9, 5])
Output: 9

Input: arr = np.array([-8, -2, -15, -1, -10])
Output: -1
"""

"""
arr = np.array([-8, -2, -15, -1, -10])
max_ele = np.max(arr)
print(max_ele)
"""


"""
Find the Mean of a Numpy Array

Input: arr = np.array([2, 4, 6, 8, 10])
Output: 6.0
Input: arr = np.array([1, 3, 5, 7])
Output: 4.0
"""
"""
arr = np.array([2, 4, 6, 8, 10])
mean_ele = np.mean(arr)
print(mean_ele)
"""


"""
Reshape a Numpy Array

Input: arr = np.array([1, 2, 3, 4, 5, 6]), rows = 2, cols = 3
Output: array([[1, 2, 3],[4, 5, 6]])
Input: arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]), rows = 4, cols = 2
Output: array([[1, 2],[3, 4],[5, 6],[7, 8]])

"""
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(4,2))
"""


"""
Standard Deviation of a Numpy Array

Input: arr = np.array([1, 2, 3, 4, 5])
Output: 1.4142135623730951
Input: arr = np.array([2, 2, 2, 2])
Output: 0.0
"""
"""
arr = np.array([2, 2, 2, 2])
print(np.std(arr))
"""


"""
Element-wise Exponentiation

Input: arr = np.array([1, 2, 3, 4]), e = 2
Output: array([ 1,  4,  9, 16])
Explanation: Each element of the array is raised to the power 2: [1², 2², 3², 4²] = [1, 4, 9, 16]
Input: arr = np.array([2, 3, 5, 7]), e = 3
Output: array([ 8, 27, 125, 343])
Explanation: Each element of the array is raised to the power 3: [2³, 3³, 5³, 7³] = [8, 27, 125, 343]
"""
"""
arr = np.array([1, 2, 3, 4])
print(np.power(arr, 2))
"""


"""
Array Concatenation

Input: arr1 = np.array([1, 2, 3]), arr2 = np.array([4, 5, 6]), axis = 0
Output: array([1, 2, 3, 4, 5, 6])
Explanation: The arrays [1, 2, 3] and [4, 5, 6] are concatenated along axis 0.
Input: arr1 = np.array([[1, 2], [3, 4]]), arr2 = np.array([[5, 6], [7, 8]]), axis = 1
Output: array([[1, 2, 5, 6], [3, 4, 7, 8]])
"""
"""
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.concat((arr1, arr2), axis=0)
print(arr3)
"""

"""
Reverse Order of Rows of a 2D Numpy Array

Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[ : :-1])
"""

"""
Diagonal in a 2D Numpy Array

Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.diagonal(arr))
"""


"""
Create a 3D Array from a List of Lists

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
"""
"""
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(np.array(data))
"""


"""
Accessing a Specific Element in a 3D Array
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), index = (1, 0, 1)
"""
"""
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)
print(arr[1][0][1])
"""



"""
Find the Maximum Element along Each Axses in a 3D Array
array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
"""
"""
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(np.max(arr, axis=0))
print(np.max(arr, axis=1))
"""


"""
Flatten a 3D Array into a 1D Array
Input: arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
Output: array([1, 2, 3, 4, 5, 6, 7, 8])
"""
"""
arr = np.array([[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]])
print(arr)

print(arr.flatten())
"""


# Find the number of rows and columns of a given matrix using NumPy
# arr = np.array([[9, 9, 9], [8, 8, 8]])
# print(arr.shape)

# Adding and Subtracting Matrices in Python
# A = [[1,2],[3,4]]
# B = [[4,5],[6,7]]
# print(np.add(A,B))


# Matrix Multiplication in NumPy
# A = [[1, 2], [2, 3]]
# B = [[4, 5], [6, 7]]

# print(np.matmul(A,B))


# Ways to Add Row/Columns in Numpy Array - Python














