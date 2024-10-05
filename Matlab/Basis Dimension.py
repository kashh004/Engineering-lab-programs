# Computation of basis and dimension for a vector space and graphical representation of linear transformation
from sympy import Matrix

# Example: Vectors in R^3
v1 = Matrix([1, 0, 0])
v2 = Matrix([0, 1, 0])
v3 = Matrix([0, 0, 1])

# Basis and dimension
V = Matrix.hstack(v1, v2, v3)
dimension = V.rank()
dimension
