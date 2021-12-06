from numpy import *
import numpy as np
# matrix 1
m = int(input("enter no: row for matrix 1 :"))
n = int(input("enter no: col for matrix 1 :"))
print("enter "  , m*n ," elements :")
arr = np.array([])
for i in range(m*n) :
        value = int(input())
        arr = append(arr,value)
arr = arr.astype(int)
matrix1 = np.array(arr).reshape(m, n)

# matrix 2

p = int(input("enter no: row for matrix 2 :"))
q = int(input("enter no: col for matrix 2 :"))
print("enter "  , p*q ," elements :")
arr1 = np.array([])
for i in range(p*q) :
        value = int(input())
        arr1 = append(arr1,value)
arr1 = arr1.astype(int)
matrix2 = np.array(arr1).reshape(p, q)

# printing matrix

print("Entered matrices :")
print("matrix 1 :")
print(matrix1)
print("matrix 2 :")
print(matrix2)

# Matrix Operations
add = np.add(matrix1,matrix2)
sub = np.subtract(matrix1,matrix2)
mul = np.multiply(matrix1,matrix2)
div = np.divide(matrix1,matrix2)
print("matrix1 + matrix2 = " )
print(add)
print("matrix1 - matrix2 = " )
print(sub)
print("matrix1 * matrix2 = " )
print(mul)
print("matrix1 / matrix2 = " )
print(div)


