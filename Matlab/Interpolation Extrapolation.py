# Interpolation/Extrapolation using Newton’s forward and backward difference formula
import numpy as np

# Example points
x = np.array([1, 2, 3])
y = np.array([1, 4, 9])

# Forward difference method
def forward_difference(x, y):
    n = len(y)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i+1, j-1] - diff_table[i, j-1]
    return diff_table

# Example usage
forward_difference(x, y)
