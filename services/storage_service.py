# Here we store all students data in memory

students = []

def phone_exists(phone):
    for s in students:
        if s.phone == phone:
            return True
    return False

def add_student(student):
    students.append(student)

def get_all_students():
    return students

def get_count():
    return len(students)
