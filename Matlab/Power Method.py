# Compute eigenvalues and eigenvectors using Rayleigh power method
import numpy as np

def power_method(A, num_iterations=1000):
    b_k = np.random.rand(A.shape[1])
    for _ in range(num_iterations):
        # Calculate matrix-by-vector product
        b_k1 = np.dot(A, b_k)
        # Recalculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        # Re-normalize the vector
        b_k = b_k1 / b_k1_norm
    # Eigenvalue
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    return eigenvalue

# Example matrix
A = np.array([[4, 1], [2, 3]])
power_method(A)
