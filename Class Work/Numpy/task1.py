import numpy as np

# task :1 Get the following array using intrinsic methods and slicing: using np.ones +slicing  + update

arr1 = np.ones((5,5), dtype=int)

arr1[1:4, 1:4] = 0
# print(arr1)

# task :2 array shown below using advanced indexing : using  np.arange + slicing 
"""
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	
"""

arr2 = np.arange(1,31).reshape(6,5)
# print(arr2)

arr3 = arr2[2:4, 0:2]
# print(arr3)


"""
task :3 using  np.arange()  create the array  (5,6)
input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	

output  :[2,8,14,20] 
"""

"""
arr4 = np.arange(1,31).reshape(6,5)
print(arr4)

arr5 = arr4[[0,1,2,3], [1,2,3,4]]
print(arr5)
"""

"""
task :4  using  np.arange()  create the array  (5,6)
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	

output : [[4,5],
	  [24,25],
	  [29,30]]
"""


arr6 = np.arange(1, 31).reshape(6,5)
# print(arr6)
# arr8 = arr6[[0,4,5], 3:5]
# arr8 = arr6[[0,4,5]][ : ,[3,4]]
# print(arr8)

