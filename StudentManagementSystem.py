class Student:
    def __init__(self, name, usn, age, branch):
        self.name = name
        self.usn = usn
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Name   : {self.name}")
        print(f"USN    : {self.usn}")
        print(f"Age    : {self.age}")
        print(f"Branch : {self.branch}")
        print("-" * 35)


students = []


def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    usn = input("Enter USN: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")

    students.append(Student(name, usn, age, branch))
    print("Student Added Successfully!\n")


def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found!\n")
        return

    for s in students:
        s.display()


def search_student():
    print("\n--- Search Student ---")
    usn = input("Enter USN to search: ")

    for s in students:
        if s.usn == usn:
            print("Student Found:")
            s.display()
            return

    print("Student not found!\n")


def delete_student():
    print("\n--- Delete Student ---")
    usn = input("Enter USN to delete: ")

    for s in students:
        if s.usn == usn:
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
