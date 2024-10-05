# Solution of system of linear equations using Gauss-Seidel iteration
import numpy as np

def gauss_seidel(A, B, x0, tolerance=1e-10, max_iterations=100):
    n = len(B)
    x = x0
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (B[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
    return x

# Example
A = np.array([[4, 1], [2, 3]])
B = np.array([1, 2])
x0 = np.zeros_like(B)
gauss_seidel(A, B, x0)
