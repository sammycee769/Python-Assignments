class CourseSummary:
    def __init__(self,course_name):
        self.__course_name = course_name
        self.__grade = None

    def set_grade(self,grade):
        self.__grade_validator(grade)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def get_course_name(self):
        return self.__course_name

    def __grade_validator(self,grade):
        if grade < 0 or grade > 100:
            raise ValueError('Grade must be between 0 and 100')
        return grade