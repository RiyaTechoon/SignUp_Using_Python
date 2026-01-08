from ui.console_form import get_student_form
from services.storage_service import add_student, get_all_students, get_count

def show_students():
    students = get_all_students()
    if not students:
        print("\nNo students registered yet.\n")
        return

    print("\n====== Registered Students ======")
    for i, s in enumerate(students, 1):
        print(f"\nStudent {i}")
        print("First Name:", s.first)
        print("Middle Name:", s.middle)
        print("Last Name:", s.last)
        print("Gender:", s.gender)
        print("DOB:", s.dob)
        print("Phone:", s.phone)
        print("Course:", s.course)

def main():
    print("===== Student Registration System =====")

    while True:
        print("\n1. Register Student")
        print("2. View Registered Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student = get_student_form()
            add_student(student)

            print("\n-------------------------------")
            print(f"Hello {student.first} 👋 You are registered!")
            print("Below are your details:")
            print("First Name:", student.first)
            print("Middle Name:", student.middle)
            print("Last Name:", student.last)
            print("Gender:", student.gender)
            print("DOB:", student.dob)
            print("City:", student.city)
            print("Phone:", student.phone)
            print("Course:", student.course)
            print("-------------------------------")
            print("Total Registered Students:", get_count())

        elif choice == "2":
            show_students()

        elif choice == "3":
            print("\nExiting... Thank you 🙏")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
