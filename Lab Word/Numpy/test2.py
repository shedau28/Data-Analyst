# Numpy cheat sheet
import numpy as np
# -------------------------------FOR ARRAYS-------------------------

# print(np.zeros((3,3), dtype=int))
# print(np.ones((4,4), dtype=float))
# print(np.full((4,3),fill_value=1, dtype=float))

# print(np.arange(1,10,1))
# print(np.linspace(1,5,3))
# print(np.eye(4,3))
# print(np.random.random((2,3)))
# print(np.empty((4,4)))


a = np.array([1,2,3])

b = np.array([(1.5,2, 3), (4,5, 6)], dtype = float)

c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)
# print(a)
# print(b)
print("============================================================")
# print(c)
# print(b+c)


# np.add
# np.subtract
# print(np.exp(b))

# x = a.view()
# y = a.copy()
# z = np.copy(a)

# print(b)
# print(np.transpose(b))


# print(c)
# print("============================================================")
# y = c.ravel()
# z = c.flatten()
# c[0,0] = 0
# print(y)
# print("============================================================")
# print(z)
# print("============================================================")
# print(c)


# print("============================================================")
# print(a)
# print("============================================================")
# print(c)
# print("============================================================")

# print(np.vstack((a,c)))
# print(np.hstack((a,b)))



# print(np.hsplit(a,3))
# print(np.vsplit(b,2))




