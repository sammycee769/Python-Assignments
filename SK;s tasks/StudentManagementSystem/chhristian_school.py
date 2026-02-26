from StudentManagement import StudentManagement


def admin_menu(student_management):

    while True:
        print("\n===== ADMIN MENU =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. View Student")
        print("4. Enroll Student in Course")
        print("5. Assign Grade")
        print("6. View Student Courses")
        print("7. Total Students")
        print("0. Back")

        choice = input("Enter your choice: ")

        try:
            match choice:

                case "1":
                    username = input("Enter username: ")
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    email = input("Enter email: ")

                    student_management.add_student(username, name, age, email)
                    print(f"Student {username} added successfully.")

                case "2":
                    username = input("Enter username: ")

                    print("Leave blank if you don't want to update.")
                    name = input("Enter new name: ")
                    age_input = input("Enter new age: ")
                    email = input("Enter new email: ")

                    name = name if name else None
                    age = int(age_input) if age_input else None
                    email = email if email else None

                    student_management.update_student(username, name, age, email)
                    print(f"Student {username} updated successfully.")

                case "3":
                    username = input("Enter username: ")
                    student = student_management.get_student(username)

                    if student is None:
                        print("Student not found.")
                    else:
                        print("\nStudent Details")
                        print("Username:", student.get_username())
                        print("Name:", student.get_name())
                        print("Age:", student.get_age())
                        print("Email:", student.get_email())

                case "4":
                    username = input("Enter username: ")
                    course = input("Enter course name: ")

                    student_management.enroll_student(username, course)
                    print(f"Student {username} enrolled successfully.")

                case "5":
                    username = input("Enter username: ")
                    course = input("Enter course name: ")
                    grade = input("Enter grade: ")

                    student_management.assign_grade(username, course, grade)
                    print("Grade assigned successfully.")

                case "6":
                    username = input("Enter username: ")
                    courses = student_management.get_student_courses(username)

                    if not courses:
                        print("No courses found.")
                    else:
                        for course in courses:
                            print("-", course)

                case "7":
                    print("Total students:", student_management.get_total_students())

                case "0":
                    break

                case _:
                    print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)


def student_menu(student_management):

    username = input("Enter your username: ")
    student = student_management.get_student(username)

    if student is None:
        print("Student not found.")
        return

    while True:

        print("\n===== STUDENT PORTAL =====")
        print("1. View My Details")
        print("2. View My Courses")
        print("0. Logout")

        choice = input("Enter choice: ")

        match choice:

            case "1":
                print("Name:", student.get_name())
                print("Age:", student.get_age())
                print("Email:", student.get_email())

            case "2":
                courses = student.get_courses()

                if not courses:
                    print("No courses enrolled.")
                else:
                    for course in courses:
                        print("-", course.get_course_name())

            case "0":
                break

            case _:
                print("Invalid choice.")


def main():

    student_management = StudentManagement()

    while True:

        print("\n===== STUDENT SYSTEM =====")
        print("1. Admin")
        print("2. Student Login")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                admin_menu(student_management)

            case "2":
                student_menu(student_management)

            case "0":
                print("Exiting system...")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
