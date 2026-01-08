from datetime import datetime

def validate_name(name):
    return name.isalpha() and len(name) >= 2

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_dob(dob):
    try:
        # Accept DD-MM-YYYY format
        date = datetime.strptime(dob, "%d-%m-%Y")
        return date <= datetime.now()
    except:
        return False
