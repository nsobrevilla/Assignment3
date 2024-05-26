# Example 1: Saving and Loading with np.save
import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
np.save('array1.npy', array1)
load_array1 = np.load('array1.npy')
print("Loaded array from array1.npy:", load_array1)

# Example 2: Saving and Loading with np.savetxt
array2 = np.array([[2, 4, 6], [8, 10, 12]])
np.savetxt('array2.txt', array2, delimiter=',')
load_array2 = np.loadtxt('array2.txt', delimiter=',')
print('Loaded array from array2.txt:', load_array2)

# Example 3: Saving and Loading with np.savez

array3 = np.array([10, 12, 14, 16, 18])
array4 = np.array([[1, 2, 3], [4, 5, 6]])

np.savez('Example3_arrays.npz', array3=array3, array4=array4)
data = np.load('Example3_arrays.npz')

loaded_array3 = data['array3']
loaded_array4 = data['array4']
print('Loaded array3 from Example3_arrays.npz:', loaded_array3)
print('Loaded array4 from Example4_arrays.npz:', loaded_array4)