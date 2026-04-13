# student-management-system
“A simple Python program to manage student records using JSON file storage. This project allows you to add students, view their details, and check results based on pass marks.”


# 📌 Features

Add new students with name and marks

View all students in a tabular format

Check results (PASS/FAIL) based on a configurable pass mark

Data stored in a JSON file (file.json)******

# Run the script:

python student_management.py


# ⚙️ Notes

The program will automatically create file.json when you add the first student.

file.json is excluded from GitHub using .gitignore since it only stores runtime data.

Example .gitignore content:

#Ignore runtime data
file.json

#Ignore Python cache
__pycache__/
*.pyc
*.pyo

#Ignore virtual environment folders
venv/
.venv/

#Ignore IDE/editor settings
.vscode/
.idea/

# 🚀 Future Improvements

Add search functionality

Implement student deletion

Create a GUI version using Tkinter or PyQt

Connect to a database (MySQL/PostgreSQL)
