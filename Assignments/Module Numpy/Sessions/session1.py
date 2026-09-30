import numpy as np

"""
2.In your script, measure and print the memory usage (in bytes) of both the Python list and the NumPy array containing 1000 integers.<br><br><em><strong>Hint:</strong> Use the sys.getsizeof() function for the list and the nbytes attribute for the NumPy array.</em>

3.Write a function compare_addition_speed() that adds 5 to every element in both a Python list and a NumPy array of 10,000 integers, and prints the time taken for each.<br><br><em><strong>Hint:</strong> Use the time module to measure execution time.</em>

4.Explain with code how vectorized operations in NumPy can replace for-loops when multiplying all elements of an array by 2. Show both the loop and the vectorized version using a Zomato-style example: multiplying all restaurant ratings by 2.
"""

# 1.Install NumPy using pip and write a Python script list_vs_array.py that creates a list and a NumPy array, each containing the numbers from 1 to 1000.


'''
list1 = [i for i in range(1, 1001)]
# print(list1)

arr1 = np.array(list1)
# print(arr1)
'''

# 2.In your script, measure and print the memory usage (in bytes) of both the Python list and the NumPy array containing 1000 integers. Use the sys.getsizeof() function for the list and the nbytes attribute for the NumPy array.
'''
list1 = [i for i in range(1, 1001)]
# print(list1)
arr1 = np.array(list1)
# print(arr1)
size_of_arr = arr1.nbytes
print(size_of_arr)
'''

# 3.Write a function compare_addition_speed() that adds 5 to every element in both a Python list and a NumPy array of 10,000 integers, and prints the time taken for each. Use the time module to measure execution time.


