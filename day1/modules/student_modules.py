from modules.result_calculator import calculate_percentage
student_name = input("Enter student name: ")
marks_python = float(input("Enter Python marks: "))
marks_math = float(input("Enter Mathematics marks: "))
marks_comm = float(input("Enter Communication marks: "))
percentage = calculate_percentage(
 marks_python,
 marks_math,
 marks_comm
)
print("\n--- Result ---")
print(f"Student: {student_name}")
print(f"Percentage: {percentage}")