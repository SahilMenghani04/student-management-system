import json
import os

File = "file.json"
Pass_marks = 40

def load_students():
    if not os.path.exists(File):
        return []
    with open(File, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_students(students):
    with open(File, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)


def add_student():
    name = input("Enter Student Name: ").strip()
    try:
        marks = int(input("Enter Student Marks: ").strip())
    except ValueError:
        print("Marks must be an integer.")
        return
    students = load_students()
    students.append({"name": name, "marks": marks})
    save_students(students)
    print("Student added.")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    print(f"{'S.No':<5} {'Name':<20} {'Marks':>5}")
    print("-" * 32)
    for i, s in enumerate(students, 1):
        print(f"{i:<5} {s['name']:<20} {s['marks']:>5}")

def check_result():
    students = load_students()
    if not students:
        print("No students found.")
        return
    print(f"{'Name':<20} {'Marks':>5} {'Result':>8}")
    print("-" * 36)
    for s in students:
        result = "PASS" if s["marks"] >= Pass_marks else "FAIL"
        print(f"{s['name']:<20} {s['marks']:>5} {result:>8}")

def main():
    while True:
        print("\n1. ADD STUDENT  2. VIEW STUDENTS  3. CHECK RESULT  4. EXIT")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            check_result()
        elif choice == "4":
            break
        else:
            print("Enter 1-4.")

if __name__ == "__main__":
    main()





    
