import numpy as np

# arr = np.array([1,2,3])
# arr = np.array([[1,2,3], [4,5,6]])

# inspect array 
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.itemsize)

# arr = np.zeros((4,4), dtype=int)

# arr = np.ones((4,3), dtype=int)

# arr = np.full((3,4), fill_value=10, dtype=int)

# arr = np.linspace(1, 10, 4)

# arr = np.arange(1,10).reshape(3,3)

# arr = np.random.rand(99,99)
# np.random.seed(10)
# arr = np.random.randint(1,10, (3,3))

# arr = np.random.choice(["Suyog","Jay","Kartik",1,2,3, 4, 5], 12).reshape(4,3)

arr = np.array([1,2,3])
arr2 = np.array([[4,5,6], [7,8,9]])

# print(np.array_split(arr, 2))

# print(np.concatenate((arr, arr2), axis=1))

# print(np.subtract(arr2, arr))

# print(np.vstack((arr, arr2)))
# print(np.hstack((arr, arr2)))

arr3 = arr.flatten()
arr4 = arr.ravel()

arr[0] = 2

print(arr3)
print(arr4)









