# Question 1(a): Read student details, display total marks and percentage

class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks
    
    def calculate_total_and_percentage(self):
        total = sum(self.marks)
        percentage = (total / 300) * 100
        return total, percentage

name = input("Enter student's name: ")
usn = input("Enter USN: ")
marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]

student = Student(name, usn, marks)
total, percentage = student.calculate_total_and_percentage()

print(f"Student Name: {student.name}, USN: {student.usn}")
print(f"Total Marks: {total}, Percentage: {percentage:.2f}%")
