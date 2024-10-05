# Question 1(b): Check if a person is a senior citizen

name = input("Enter name: ")
year_of_birth = int(input("Enter year of birth: "))
current_year = 2024
age = current_year - year_of_birth

if age >= 60:
    print(f"{name} is a senior citizen.")
else:
    print(f"{name} is not a senior citizen.")
