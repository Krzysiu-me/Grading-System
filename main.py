students = {}


def add_student(name):
    if name.isnumeric():
        print("Student name cannot be purely numeric. Please enter a valid name.")
    else:
        students[name] = []
        print(f"Student {name} added successfully.")


def input_grade(name, grade):
    if name in students:
        if 0 <= grade <= 100:
            students[name].append(grade)
            print(f"Grade {grade} added for {name}.")
        else:
            print("Grade must be between 0 and 100. Please enter a valid grade.")
    else:
        print("Student not found!")


def calculate_average_grade(name):
    if name in students:
        grades = students[name]
        if grades:
            avg_grade = sum(grades) / len(grades)
            print(f"Average grade for {name}: {avg_grade}")
        else:
            print(f"No grades found for {name}.")
    else:
        print("Student not found!")


def print_menu():
    print("Welcome to the Student Grading System")
    print("1. Add a new student")
    print("2. Input grade for a student")
    print("3. Calculate average grade for a student")
    print("4. Quit")


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
    print_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter the student's name: ")
        add_student(name)
    elif choice == "2":
        name = input("Enter the student's name: ")
        grade = get_valid_float("Enter the grade: ")
        input_grade(name, grade)
    elif choice == "3":
        name = input("Enter the student's name: ")
        calculate_average_grade(name)
    elif choice == "4":
        print("Thank you for using the Student Grading System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
