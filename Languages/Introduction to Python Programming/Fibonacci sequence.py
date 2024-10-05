# Question 2(a): Generate Fibonacci sequence of length N

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the length of Fibonacci sequence: "))
print(fibonacci(n))
