from student import Student
from student_manager import StudentManager
from storage import load_students, save_students


manager = StudentManager()
student = students()

# TODO: Load students from students.json


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
        # TODO: Read student details
        # TODO: Create a Student object
        # TODO: Add the student to the manager
        # TODO: Save students
        pass

    elif choice == "2":
        # TODO: View students
        pass

    elif choice == "3":
        # TODO: Read a name
        # TODO: Find the student
        # TODO: Display the student if found
        pass

    elif choice == "4":
        # TODO: Read the student name and new marks
        # TODO: Update the student
        # TODO: Save students
        pass

    elif choice == "5":
        # TODO: Read the student name
        # TODO: Delete the student
        # TODO: Save students
        pass

    elif choice == "6":
        print("Exiting application.")
        break

    else:
        print("Invalid choice.")
