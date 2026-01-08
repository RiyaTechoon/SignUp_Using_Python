# 🎓 Student Registration System (Console App)

A **menu-driven console application** in Python to register students, validate inputs, and view registered student details.  
This project is **modular, easy to read, and professional**, perfect for learning Python OOP and building scalable console apps.

---

## Features

- ✅ Menu-based interface  
- ✅ Input validation:  
  - Names must contain only letters  
  - Phone number must be 10 digits  
  - Date of Birth cannot be in the future (DD-MM-YYYY)  
- ✅ Live registration count  
- ✅ Modular and professional project structure  
- ✅ Easy to expand (add database or web UI)  

---

## 📂 Project Structure
│
├── app.py # Main program / entry point
├── models/
│ └── student.py # Student data model
├── services/
│ └── storage_service.py # Handles storage of students and count
├── validations/
│ └── student_validations.py # Input validation functions
└── ui/
└── console_form.py # Console-based form input / UI

