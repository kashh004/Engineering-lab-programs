# Program to compute area, surface area, volume, and center of gravity
from sympy import symbols, pi

# Example: Area and Volume of a Sphere with radius r
r = symbols('r')
surface_area = 4 * pi * r**2
volume = (4/3) * pi * r**3
surface_area, volume
