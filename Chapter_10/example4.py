# Example 10.4
# Matrix Multiplication - General
import numpy as np
m = eval(input("Type number of rows in Matrix A:"))
p = eval(input("Type number of columns in Matrix A:"))
matrix_A = np.zeros((m, p))
for i in range(0,m):
  for j in range(0,p):
    matrix_A[i][j] = eval(input("Type an element of Matrix A:"))
p = eval(input("Type number of rows in Matrix B:"))
n = eval(input("Type number of columns in Matrix B:"))
matrix_B = np.zeros((p, n))
for i in range(0,p):
  for j in range(0,n):
    matrix_B[i][j] = eval(input("Type an element of Matrix B:"))
matrix_C = np.zeros((m, n))

matrix_C = np.dot(matrix_A,matrix_B)

for i in range(0,m):
  for j in range(0,n):
    print(f"Element at ({i},{j})of Matrix C is: {matrix_C[i][j]}")