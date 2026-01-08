from validations.student_validations import validate_name, validate_dob, validate_phone
from models.student import Student

def get_valid_input(prompt, validation_func, error_msg):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        print(error_msg)

def get_student_form():
    print("\n----- Student Registration Form -----")

    first = get_valid_input("Enter your First Name: ", validate_name, "Invalid First Name")
    middle = input("Enter your Middle Name (optional): ")
    last = get_valid_input("Enter your Last Name: ", validate_name, "Invalid Last Name")
    dob = get_valid_input("DOB (DD-MM-YYYY): ", validate_dob, "Invalid DOB or future date")
    phone = get_valid_input("Phone (10 digits): ", validate_phone, "Invalid Phone")
    course = input("Desired Course: ")

    return Student(first, middle, last, dob, phone, course)
