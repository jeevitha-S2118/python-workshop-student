from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
manager = StudentManager()
# Load students from students.json
manager.students = load_students("students.json", Student)
while True:
 print("\n===== Student Management System =====")
 print("1. Add Student")
 print("2. View Students")
 print("3. Find Student")
 print("4. Update Student")
 print("5. Delete Student")
 print("6. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
 # Read student details
 name = input("Enter student name: ")
 age = int(input("Enter student age: "))
 python = float(input("Enter Python marks: "))
 mathematics = float(input("Enter Mathematics marks: "))
 communication = float(input("Enter Communication marks: "))
 # Create a Student object
 student = Student(
 name,
 age,
 python,
 mathematics,
 communication
 )
 # Add the student to the manager
 manager.add_student(student)
 # Save students
 save_students(manager.students, "students.json") print("Student added successfully.")
 elif choice == "2":
 # View students
 manager.view_students()
 elif choice == "3":
 # Read a name
 name = input("Enter student name: ")
 # Find the student
 student = manager.find_student(name)
 # Display the student if found
 if student:
 student.display()
 else:
 print("Student not found.")
 elif choice == "4":
 # Read the student name and new marks
 name = input("Enter student name: ")
 python = float(input("Enter new Python marks: "))
 mathematics = float(input("Enter new Mathematics marks: "))
 communication = float(input("Enter new Communication marks: "))
 # Update the student
 if manager.update_student(
 name,
 python,
 mathematics,
 communication
 ):
 # Save students
 save_students(manager.students, "students.json")
 print("Student updated successfully.")
 else:
 print("Student not found.")
 elif choice == "5":
 # Read the student name
 name = input("Enter student name: ")
 # Delete the student
 if manager.delete_student(name):
 # Save students
 save_students(manager.students, "students.json")
 print("Student deleted successfully.")
 else:
 print("Student not found.")
 elif choice == "6":
 print("Exiting application.")
 break
 else:
 print("Invalid choice.")