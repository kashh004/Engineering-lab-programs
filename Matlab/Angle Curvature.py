# Finding angle between polar curves, curvature, and radius of curvature
from sympy import symbols, diff, cos
import numpy as np

# Polar curves r1 = 1 + cos(theta), r2 = 1 - cos(theta)
theta = symbols('theta')
r1 = 1 + cos(theta)
r2 = 1 - cos(theta)

# Derivatives of r1 and r2
dr1_dtheta = diff(r1, theta)
dr2_dtheta = diff(r2, theta)

# Calculate angle between curves at a point (substitute specific value for theta)
angle_between_curves = np.arctan(abs((dr1_dtheta - dr2_dtheta) / (1 + dr1_dtheta * dr2_dtheta)))
angle_between_curves

# Example curvature for y = x^2
x = symbols('x')
y = x**2
y_prime = diff(y, x)
y_double_prime = diff(y_prime, x)
curvature = abs(y_double_prime) / (1 + y_prime**2)**(3/2)
curvature
