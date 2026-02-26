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