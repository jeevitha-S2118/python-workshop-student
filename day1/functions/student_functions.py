# Day 1 - Python Fundamentals
student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:")
# Create a function to calculate the percentage
def calculate_percentage(python, mathematics, communication):
 total = python + mathematics + communication
 percentage = total / 3
 return percentage
percentage = calculate_percentage(
 marks_python,
 marks_math,
 marks_comm
)
print("\n -- Result --")
print("Student:", student_name)
print("Percentage:", percentage)