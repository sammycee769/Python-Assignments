from Student import Student
from CourseSummary import CourseSummary
import re

class StudentManagement:
    def __init__(self):
        self.__students = {}

    def add_student(self,student_username ,name,age,email):
        self.__duplicate_student_validator(student_username)
        age = self.__age_validator(age)
        email = self.__email_validator(email)

        self.__students[student_username] = Student(student_username,name,age,email)

    def update_student(self,student_username,name = None,age = None,email = None):
        student = self.__students.get(student_username)
        self.__student_validator(student)

        new_name = name if name is not None else student.__Student_name
        new_age = age if age is not None else student.__Student_age
        new_email = email if email is not None else student.__Student_email

        student.update_details(new_name,new_age,new_email)

    def get_student(self,student_username):
        return self.__students.get(student_username)

    def get_total_students(self):
        return len(self.__students)

    def enroll_student(self,student_username,course_name):
        student = self.__students.get(student_username)
        self.__student_validator(student)

        self.__duplicate_course_validator(student, course_name)
        enrolled_course = CourseSummary(course_name)
        student.set_courses(enrolled_course)


    def assign_grade(self,student_username,course_name,grade):
        student = self.__students.get(student_username)
        self.__student_validator(student)

        course = self.__course_validator(student, course_name)
        course.set_grade(grade)

    def get_student_courses(self,student_username):
        student = self.__students.get(student_username)
        self.__student_validator(student)
        return [course.get_course_name() for course in student.get_courses()]

    def __duplicate_student_validator(self,student_username):
        if student_username  in self.__students:
            raise ValueError("Student already exists")

    def __age_validator(self, age):
        if age <= 0 or age > 30:
            raise ValueError("Age must be between 0 and 30")
        return age

    def __email_validator(self, email):
        if re.fullmatch(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}', email):
            return email
        else:
            raise ValueError("Invalid Email Address")

    def __duplicate_course_validator(self, student, course_name):
        for course in student.get_courses():
            if course.get_course_name() == course_name:
                raise ValueError("Student already enrolled in this course")

    def __student_validator(self,student):
        if student is None:
            raise ValueError("Student does not exist")

    def __course_validator(self, student, course_name):
        for course in student.get_courses():
            if course.get_course_name() == course_name:
                return course
        raise ValueError("Course does not exist")



