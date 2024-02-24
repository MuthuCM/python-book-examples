# Example 10.3
# Matrix Multiplication - Specific Case
import numpy as np
# Take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

# Result will be 3x4 matrix

C = np.zeros((3,4))

C = np.dot(A,B)

for row in C:
    print(row)