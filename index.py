import sqlite3

conn = sqlite3.connect("school.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone NUMBER NOT NULL,
        grade_level TEXT NOT NULL,
        parent_name TEXT NOT NULL,
        parent_phone NUMBER NOT NULL
    )
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        department TEXT NOT NULL
    )
""")
conn.commit()

def view_student_info():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("Student Information")
    print("-------------------")
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Email:", row[2])
        print("Phone:", row[3])
        print("-------------------\n")


def add_student():
    name = input("Enter the student's name: ")
    email = input("Enter the student's email address: ")
    phone = input("Enter the student's phone number: ")
    grade_level = input("Enter the student's Grade_level: ")
    parent_name = input("Enter Father's Name: ")
    parent_phone = input("Enter the Father's Phone Number: ")

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, phone, grade_level, parent_name, parent_phone) VALUES (?, ?, ?, ?, ?, ?)", (name, email, phone, grade_level, parent_name, parent_phone))
    conn.commit()

    print("Student added successfully.")

def update_student_info():
    student_id = int(input("Enter the ID of the student to update: "))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()

    if row:
        name = input(
            "Enter the student's name (leave blank to keep current value: ")
        email = input(
            "Enter the student's email address (leave blank to keep current value: ")
        phone = input(
            "Enter the student's phone number (leave blank to keep current value: ")
        if name:
            cursor.execute(
                "UPDATE students SET name=? WHERE id=?", (name, student_id))
        if email:
            cursor.execute(
                "UPDATE students SET email=? WHERE id=?", (email, student_id))
        if phone:
            cursor.execute(
                "UPDATE students SET phone=? WHERE id=?", (phone, student_id))

        conn.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    print("Student deleted successfully.")


def view_teacher_info():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers")
    rows = cursor.fetchall()
    print("Teacher Information")
    print("-------------------")
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Email:", row[2])
        print("Phone:", row[3])
        print("Department:", row[4])
        print("-------------------\n")


def add_teacher():
    name = input("Enter the teacher's name: ")
    email = input("Enter the teacher's email address: ")
    phone = input("Enter the teacher's phone number: ")
    department = input("Enter the teacher's department: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers(name, email , phone, department) VALUES (?, ?, ?, ?)",
                   (name, email, phone, department))
    conn.commit()

    print("Teacher added successfully.")


def update_teacher_info():
    teacher_id = int(input("Enter the ID of the teacher to update: "))
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE id=?", (teacher_id,))
    row = cursor.fetchone()

    if row:
        name = input(
            "Enter the teacher's name (leave blank to keep current value: ")
        email = input(
            "Enter the teacher's email address (leave blank to keep current value: ")
        phone = input(
            "Enter the teacher's phone number (leave blank to keep current value: ")
        department = input(
            "Enter the teacher's department (leave blank to keep current value: ")
        if name:
            cursor.execute(
                "UPDATE teachers SET name=? WHERE id=?", (name, teacher_id))
        if email:
            cursor.execute(
                "UPDATE teachers SET email=? WHERE id=?", (email, teacher_id))
        if phone:
            cursor.execute(
                "UPDATE teachers SET phone=? WHERE id=?", (phone, teacher_id))
        if department:
            cursor.execute(
                "UPDATE teachers SET department=? WHERE id=?", (department, teacher_id))

        conn.commit()
        print("Teacher updated successfully.")
    else:
        print("Teacher not found.")


def delete_teacher():
    teacher_id = int(input("Enter the ID of the teacher to delete: "))
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teachers WHERE id=?", (teacher_id,))
    conn.commit()

    print("Teacher deleted successfully.")


def student_menu():
    while True:
        print("Student Menu")
        print("------------")
        print("1. View student information")
        print("2. Add a new student")
        print("3. Update student information")
        print("4. Delete a student")
        print("5. Return to main menu\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_student_info()
        elif choice == 2:
            add_student()
        elif choice == 3:
            update_student_info()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


def teacher_menu():
    while True:
        print("Teacher Menu")
        print("------------")
        print("1. View teacher information")
        print("2. Add a new teacher")
        print("3. Update teacher information")
        print("4. Delete a teacher")
        print("5. Return to main menu\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_teacher_info()
        elif choice == 2:
            add_teacher()
        elif choice == 3:
            update_teacher_info()
        elif choice == 4:
            delete_teacher()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")



def main():
    while True:
        print("School Management System Menu")
        print("-----------------------------")
        print("1. Student Menu")
        print("2. Teacher Menu")
        print("3. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_menu()
        elif choice == 2:
            teacher_menu()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
