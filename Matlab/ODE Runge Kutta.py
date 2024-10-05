# Solution of ODE of first order and first degree by Runge-Kutta 4th order and Milne's predictor-corrector method
import numpy as np

# Runge-Kutta 4th order method
def runge_kutta(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end+h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_values, y_values

# Example usage
def f(t, y):
    return y - t**2 + 1

runge_kutta(f, 0.5, 0, 2, 0.2)
