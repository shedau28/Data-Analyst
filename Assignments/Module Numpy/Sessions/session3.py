






import numpy as np

# 1.Create a NumPy array representing the number of likes on 7 Instagram posts and print its ndim, shape, size, dtype, itemsize, and nbytes properties.

arr1 = np.random.randint(1, 1000, 7)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# print(arr1.dtype)
# print(arr1.itemsize)
# print(arr1.nbytes)

# 2.Given a 2D NumPy array of daily step counts for 5 days (each row is a day, columns are morning and evening), use reshape() to convert it into a 1D array, then back to a 2D array with 5 rows and 2 columns.<br><br><em><strong>Hint:</strong> Use the shape attribute to check your array after each reshape.</em>


arr2 = np.random.randint(1000, 9000, (5,2))
# print(arr2)
arr2 = arr2.reshape(10)
# print(arr2)
arr2 = arr2.reshape(5,2)
# print(arr2)

# 3.Build a NumPy array representing the prices of 12 food items from a Zomato order, then use ravel(), flatten(), and resize() to create different shaped versions of the data and print each result.<br><br><em><strong>Constraint:</strong> Show the difference between ravel() and flatten() in your code comments.</em>

arr3 = np.random.randint(100, 300, 12)
# print(arr3)
ravel_arr = arr3.ravel()
# print(ravel_arr)
# In ravel it sahres memory with original data.  if any changes are done to original data then it reflects in ravel too.
flat_arr = arr3.flatten()
# print(flat_arr)
# In flattern it makes copy of original data so if any changes were done to original then it wont reflect in flattern data.

# 4.Take a 3x3 NumPy array representing a mini Spotify playlist grid (rows: playlists, columns: song counts in categories like Pop, Rock, Indie). Use both T and np.transpose() to swap rows and columns, then print the transposed array.

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr4)
t_arr = arr4.T
# print(t_arr)
transpose_arr = np.transpose(arr4)
# print(transpose_arr)

# 5.Given a 1D NumPy array of 15 Flipkart product ratings, use reshape() to convert it into a 3x5 array, then use flatten() to return it to a 1D array. Explain in a comment when you would use flatten() versus ravel() in real projects.

arr5 = np.random.uniform(3,5,15)
arr5 = arr5.reshape(3,5)
# print(arr5.flatten())



