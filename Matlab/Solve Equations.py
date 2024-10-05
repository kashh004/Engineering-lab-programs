# Solution of algebraic and transcendental equations by Ramanujan’s, Regula-Falsi and Newton-Raphson method
from sympy import symbols, Eq, solve, diff

x = symbols('x')

# Example equation: x^3 - 2x - 5 = 0
equation = Eq(x**3 - 2*x - 5, 0)

# Newton-Raphson method
def newton_raphson(func, x0, tol=1e-5, max_iter=100):
    derivative = diff(func, x)
    x_n = x0
    for _ in range(max_iter):
        x_next = x_n - func.subs(x, x_n) / derivative.subs(x, x_n)
        if abs(x_next - x_n) < tol:
            return x_next
        x_n = x_next
    return None

# Example usage
newton_raphson(equation.lhs, 2)
