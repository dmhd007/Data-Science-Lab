import numpy as np
matrix = np.array([[2,4,6],[7,3,1],[4,8,2]])
column,row = matrix.shape
print("sum of diagonals:",sum(np.diag(matrix)))
# sum=0
# for i in range(row):
#     for j in range(column):
#         if i==j:
#             sum = sum + matrix[i][j]
# print("sum of diagonals:",sum)
