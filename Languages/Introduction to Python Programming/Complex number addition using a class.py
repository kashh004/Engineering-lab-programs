# Question 9: Complex number addition using a class

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

n = int(input("Enter the number of complex numbers: "))
complex_numbers = []

for i in range(n):
    real = float(input(f"Enter real part of complex number {i+1}: "))
    imag = float(input(f"Enter imaginary part of complex number {i+1}: "))
    complex_numbers.append(Complex(real, imag))

result = sum(complex_numbers, Complex(0, 0))

print(f"Sum of complex numbers: {result}")
