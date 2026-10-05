#Initialising dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")

# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print(f"Student {name} not found")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted")
    else:
        print(f"Student {name} not found")

# Display students
def display_students():
    print(student_grades)


# Menu
while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        add_student(name, grade)

    elif choice == "2":
        name = input("Enter student name: ")
        grade = input("Enter new grade: ")
        update_student(name, grade)

    elif choice == "3":
        name = input("Enter student name: ")
        delete_student(name)

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")