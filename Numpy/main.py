# numpy_tutorial.py
# A comprehensive demo of NumPy features in a single file
# Author: ChatGPT

import numpy as np

# -----------------------------
# 1. Creating arrays
# -----------------------------

# 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1d)

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2d)

# 3D array
arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D array:\n", arr3d)

# Arrays of zeros, ones, or a specific value
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones
full = np.full((2, 3), 7) # 2x3 array filled with 7

# -----------------------------
# 2. Array attributes
# -----------------------------
print("Shape of arr3d:", arr3d.shape)
print("Number of dimensions:", arr3d.ndim)
print("Data type:", arr3d.dtype)
print("Size (total elements):", arr3d.size)

# -----------------------------
# 3. Creating arrays with sequences
# -----------------------------
arr_arange = np.arange(0, 10, 2)  # start, stop, step
arr_linspace = np.linspace(0, 1, 5)  # start, stop, number of points

print("arange:", arr_arange)
print("linspace:", arr_linspace)

# -----------------------------
# 4. Reshaping arrays
# -----------------------------
arr = np.arange(12)
arr_reshaped = arr.reshape((3, 4))  # 3 rows, 4 columns
print("Reshaped array:\n", arr_reshaped)

# Flattening
arr_flat = arr_reshaped.flatten()
print("Flattened array:", arr_flat)

# -----------------------------
# 5. Indexing and slicing
# -----------------------------
print("First element of arr1d:", arr1d[0])
print("Last row of arr2d:", arr2d[-1])
print("Subarray of arr2d:\n", arr2d[:, 1:3])  # all rows, columns 1 to 2

# -----------------------------
# 6. Mathematical operations
# -----------------------------
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2 =", a ** 2)

# Universal functions
print("sin(a):", np.sin(a))
print("exp(a):", np.exp(a))
print("sqrt(a):", np.sqrt(a))

# -----------------------------
# 7. Aggregations
# -----------------------------
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum:", np.sum(arr))
print("Sum along axis 0 (columns):", np.sum(arr, axis=0))
print("Sum along axis 1 (rows):", np.sum(arr, axis=1))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# -----------------------------
# 8. Boolean indexing
# -----------------------------
arr = np.array([1, 2, 3, 4, 5])
print("Elements greater than 3:", arr[arr > 3])

# -----------------------------
# 9. Random numbers
# -----------------------------
rand = np.random.rand(2, 3)  # uniform [0,1)
rand_int = np.random.randint(0, 10, (2, 3))  # integers 0 to 9
print("Random floats:\n", rand)
print("Random integers:\n", rand_int)

# -----------------------------
# 10. Linear algebra
# -----------------------------
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:\n", np.dot(A, B))
print("Transpose:\n", A.T)
print("Determinant:", np.linalg.det(A))
print("Inverse:\n", np.linalg.inv(A))

# -----------------------------
# 11. Saving and loading arrays
# -----------------------------
np.save("array.npy", arr2d)        # save to file
loaded = np.load("array.npy")       # load from file
print("Loaded array:\n", loaded)

# -----------------------------
# End of NumPy tutorial
# -----------------------------