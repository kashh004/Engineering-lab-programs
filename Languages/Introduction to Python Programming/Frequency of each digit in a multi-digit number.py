# Question 4: Frequency of each digit in a multi-digit number

def digit_frequency(number):
    freq = {}
    for digit in number:
        if digit.isdigit():
            freq[digit] = freq.get(digit, 0) + 1
    return freq

number = input("Enter a multi-digit number: ")
freq = digit_frequency(number)

for digit, count in freq.items():
    print(f"Digit {digit}: {count} times")
