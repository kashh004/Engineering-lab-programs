# Numerical solution of a system of linear equations
import numpy as np

# Coefficient matrix A and constant vector B
A = np.array([[3, 2], [1, 2]])
B = np.array([2, 4])

# Solve system of equations Ax = B
solution = np.linalg.solve(A, B)
solution
