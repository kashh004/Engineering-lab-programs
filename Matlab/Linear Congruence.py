# Solving linear congruences ax ≡ b (mod m)
from sympy import mod_inverse

def linear_congruence(a, b, m):
    a_inv = mod_inverse(a, m)
    return (a_inv * b) % m

# Example: Solve 3x ≡ 2 (mod 7)
linear_congruence(3, 2, 7)
