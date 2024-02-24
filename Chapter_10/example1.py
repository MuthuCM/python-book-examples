# Example 10.1
# Displaying Diagonal Elements of a Matrix
import numpy as np
m = eval(input("Type number of rows:"))
n = eval(input("Type number of columns:"))
matrix_A = np.zeros((m, n))
for i in range(0,m):
  for j in range(0,n):
    matrix_A[i][j] = eval(input("Type an element:"))
for i in range(0,m):
  for j in range(0,n):
    if i == j:
      print(f"Diagonal Element ({i},{j})is: {matrix_A[i][j]}")