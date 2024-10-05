# Computation of area under the curve using Trapezoidal, Simpson’s (1/3)rd and (3/8)th rule
import numpy as np

# Example function f(x) = x^2
def f(x):
    return x**2

# Trapezoidal rule
def trapezoidal(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i*h)
    integral *= h
    return integral

# Example usage
trapezoidal(0, 1, 100)
