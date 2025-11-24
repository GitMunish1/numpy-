import numpy as np

arr1 = np.array([[[1, 3 ,34, 5543,5, 5], [2, 5,34,5, 8, 89], [2, 90, 98, 38, 89, 78]]])

print("array :", arr1)
print("dimension of array:", arr1.ndim)
print("shape of array:", arr1.shape)
print(type(arr1))
print("size of array:", arr1.size)
print(arr1[0, 2, 4]) 