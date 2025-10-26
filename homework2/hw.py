import os

STUDENTS_FILE = "students.txt"
DELETED_FILE = "deleted_students.txt"

# 1. Check if the file exists; if not, create it with sample data
if not os.path.exists(STUDENTS_FILE):
    with open(STUDENTS_FILE, "w") as f:
        f.write("John Smith, 85\nEmily Johnson, 90\nMichael Brown, 78\n")


# 2. All options
def read_students():
    try:
        with open(STUDENTS_FILE, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print("File not found.")
        return []


def show_students():
    students = read_students()
    if not students:
        print("The list is empty.")
    else:
        for s in students:
            print(s)


def add_student():
    name = input("Enter student name: ").strip()
    grade = input("Enter student grade: ").strip()
    if not grade.isdigit():
        print("Error: grade must be a number.")
        return
    with open(STUDENTS_FILE, "a") as f:
        f.write(f"{name}, {grade}\n")
    print("Student added successfully.")


def remove_student():
    name = input("Enter name to remove: ").strip().lower()
    students = read_students()
    new_list, deleted = [], []
    for s in students:
        if not s.lower().startswith(name):
            new_list.append(s)
        else:
            deleted.append(s)
    if not deleted:
        print("Student not found.")
        return
    with open(STUDENTS_FILE, "w") as f:
        f.write("\n".join(new_list) + ("\n" if new_list else ""))
    with open(DELETED_FILE, "a") as f:
        f.write("\n".join(deleted) + "\n")
    print("Student removed and saved to deleted_students.txt.")


def update_grade():
    name = input("Enter name to update: ").strip().lower()
    students = read_students()
    found = False
    for i, s in enumerate(students):
        if s.lower().startswith(name):
            new_grade = input("Enter new grade: ").strip()
            if not new_grade.isdigit():
                print("Error: grade must be a number.")
                return
            students[i] = f"{s.split(',')[0]}, {new_grade}"
            found = True
    if not found:
        print("Student not found.")
        return
    with open(STUDENTS_FILE, "w") as f:
        f.write("\n".join(students) + "\n")
    print("Grade updated successfully.")


def show_average():
    students = read_students()
    grades = [int(s.split(",")[1]) for s in students if "," in s]
    if grades:
        print(f"Class average: {sum(grades)/len(grades):.2f}")
    else:
        print("No data available.")


menu = {
    "1": show_students,
    "2": add_student,
    "3": remove_student,
    "4": update_grade,
    "5": show_average,
    "6": exit
}

while True:
    print("\nMenu:\n1. Show all students\n2. Add a new student\n3. Remove a student\n4. Update a student's grade\n5. Show class average\n6. Exit")
    choice = input("Enter your choice: ")
    action = menu.get(choice)
    if action:
        action()
    else:
        print("Invalid choice.")
