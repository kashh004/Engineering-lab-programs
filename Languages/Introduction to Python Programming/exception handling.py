# Question 8: Division with assertion and exception handling

def DivExp(a, b):
    assert a > 0, "a must be greater than 0"
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

a = float(input("Enter a: "))
b = float(input("Enter b: "))
try:
    result = DivExp(a, b)
    print(f"Result: {result}")
except Exception as e:
    print(e)
