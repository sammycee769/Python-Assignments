import re
class Student:
    def __init__(self,user_name,name,age,email):
        self.__name = name
        self.__user_name = user_name
        self.__age = self.__age_validator(age)
        self.__email = self.__email_validator(email)
        self.__course_summary = []

    def get_username(self):
        return self.__user_name

    def set_courses(self,course):
        self.__course_summary.append(course)

    def get_courses(self):
        return self.__course_summary

    def update_details(self,name,age,email):
        self.__name = name
        self.__age = self.__age_validator(age)
        self.__email = self.__email_validator(email)


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def __age_validator(self,age):
        if age <= 0 or age > 30:
            raise ValueError("Age must be between 0 and 30")
        return age
    def __email_validator(self,email):
        if re.fullmatch(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}', email):
            return email
        else:
            raise ValueError("Invalid Email Address")








