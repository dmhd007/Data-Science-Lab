import numpy as np
matrix1 = np.array([[1,3,4],[3,6,2],[5,2,4]])
matrix2 = np.array([[2,5,6],[5,3,2],[1,2,6]])

print("Matrix addition:\n",matrix1 + matrix2)
print("Matrix substraction:\n",matrix1 - matrix2)
print("Matrix multiplication:\n",np.matmul(matrix1, matrix2))
print("Matrix division:\n",np.divide(matrix1,matrix2))