# Question 10: Student class to calculate and display marks

class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks = []

    def getMarks(self):
        for i in range(3):
            mark = float(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)

    def display(self):
        total = sum(self.marks)
        percentage = (total / 300) * 100
        print(f"Name: {self.name}, USN: {self.usn}")
        print(f"Marks: {self.marks}, Total: {total}, Percentage: {percentage:.2f}%")

name = input("Enter student's name: ")
usn = input("Enter USN: ")

student = Student(name, usn)
student.getMarks()
student.display()
