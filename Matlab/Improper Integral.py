# Evaluation of improper integrals
from sympy import symbols, integrate, oo

x = symbols('x')

# Example: Integral of 1/x^2 from 1 to infinity
improper_integral = integrate(1/x**2, (x, 1, oo))
improper_integral
