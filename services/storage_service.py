# Here we store all students data in memory

students = []

def add_student(student):
    students.append(student)

def get_all_students():
    return students

def get_count():
    return len(students)
