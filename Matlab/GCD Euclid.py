# Finding GCD using Euclid's Algorithm
def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
gcd_euclid(48, 18)
