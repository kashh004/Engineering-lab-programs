# Question 3: Mean, variance, and standard deviation

import math

def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return mean, variance, std_dev

n = int(input("Enter number of values: "))
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
mean, variance, std_dev = calculate_statistics(numbers)

print(f"Mean: {mean}, Variance: {variance}, Standard Deviation: {std_dev}")
