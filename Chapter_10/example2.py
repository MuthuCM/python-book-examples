# Example 10.2
# Matrix Addition
import numpy as np
m = eval(input("Type number of rows: "))
n = eval(input("Type number of columns: "))

matrix_A = np.zeros((m, n))
for i in range(0,m):
  for j in range(0,n):
    matrix_A[i][j] = eval(input("Type an element of Matrix A:"))

matrix_B = np.zeros((m, n))
for i in range(0,m):
  for j in range(0,n):
    matrix_B[i][j] = eval(input("Type an element of Matrix B:"))

matrix_C = np.zeros((m, n))

matrix_C = np.add(matrix_A,matrix_B)

for i in range(0,m):
  for j in range(0,n):
    print(f"Element at ({i},{j})position of Matrix C is: {matrix_C[i][j]}")