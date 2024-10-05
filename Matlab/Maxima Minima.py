# Applications to Maxima and Minima of two variables
from sympy import symbols, diff, solve

# Variables
x, y = symbols('x y')

# Function f(x, y)
f = x**2 + y**2

# Partial derivatives
f_x = diff(f, x)
f_y = diff(f, y)

# Critical points
critical_points = solve([f_x, f_y], (x, y))
critical_points
