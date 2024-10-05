# Computing the inner product and orthogonality
from sympy import Matrix

# Example vectors
v1 = Matrix([1, 2])
v2 = Matrix([2, -1])

# Inner product
inner_product = v1.dot(v2)

# Orthogonality check (if inner product is zero)
orthogonal = inner_product == 0
inner_product, orthogonal
