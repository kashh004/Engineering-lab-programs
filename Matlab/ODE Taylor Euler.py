# Solution of ODE of first order and first degree by Taylor's series and Modified Euler’s method
from sympy import Function, dsolve, Eq, Derivative, symbols

t, C1 = symbols('t C1')
y = Function('y')

# Example ODE: dy/dt = y - t^2 + 1
ode = Eq(Derivative(y(t), t), y(t) - t**2 + 1)

# Solution using Taylor's series method (symbolic solution)
ode_solution = dsolve(ode, y(t))

# Example Modified Euler's method for numeric ODE solution
def modified_euler(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end+h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        y_predict = y + h * f(t, y)
        y_values[i] = y + h/2 * (f(t, y) + f(t+h, y_predict))
    
    return t_values, y_values

# Example function for dy/dt
def f(t, y):
    return y - t**2 + 1

# Example usage
modified_euler(f, 0.5, 0, 2, 0.2)
