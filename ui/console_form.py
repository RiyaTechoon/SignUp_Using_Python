from validations.student_validations import validate_name, validate_dob, validate_phone
from models.student import Student
from services.storage_service import phone_exists

# Checks for valid Input Data
def get_valid_input(prompt, validation_func, error_msg):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        print(error_msg)

def get_unique_phone():
    while True:
        phone = input("Phone (10 digits): ")
        if not validate_phone(phone):
            print("Phone must be 10 digits")
        elif phone_exists(phone):
            print("This phone number is already registered")
        else:
            return phone

# Input Form Fields for Name, DOB, Phone, Courses
def get_student_form():
    print("\n----- Student Registration Form -----")

    first = get_valid_input("Enter your First Name: ", validate_name, "Invalid First Name")
    middle = input("Enter your Middle Name (optional): ")
    last = get_valid_input("Enter your Last Name: ", validate_name, "Invalid Last Name")
    gender = input("Gender (Male/Female/Other): ")
    dob = get_valid_input("DOB (DD-MM-YYYY): ", validate_dob, "Invalid DOB or future date")
    city = input("City: ")
    phone = get_unique_phone()
    course = input("Desired Course: ")

    return Student(first, middle, last, gender, dob, city, phone, course)
