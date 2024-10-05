# Question 2(b): Factorial function and binomial coefficient

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def binomial_coefficient(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter N: "))
r = int(input("Enter R: "))
print(f"Binomial Coefficient: {binomial_coefficient(n, r)}")
