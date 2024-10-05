# Finding partial derivatives and Jacobian matrix
from sympy import symbols, diff, Matrix

# Variables
x, y = symbols('x y')

# Functions
f1 = x**2 + y**2
f2 = x*y

# Partial derivatives
df1_dx = diff(f1, x)
df1_dy = diff(f1, y)
df2_dx = diff(f2, x)
df2_dy = diff(f2, y)

# Jacobian matrix
J = Matrix([[df1_dx, df1_dy], [df2_dx, df2_dy]])
J
