import unittest
from StudentManagement import StudentManagement


class StudentManagementSystemTest(unittest.TestCase):
    def setUp(self):
        self.student_management = StudentManagement()
        self.student_management.add_student("chris101","Christian",18,"samuelchristian769@gmail.com")

    def test_that_I_add_A_new_student(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        self.student_management.add_student("sammy","Samuel",17,"sammyc769@gmail.com")
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 2)

    def test_that_I_try_to_add_a_duplicate_student_throws_error(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        with self.assertRaises(ValueError) as context:self.student_management.add_student("chris101","Christian",18,"samuelchristian769@gmail.com")
        self.assertEqual(str(context.exception), "Student already exists")

    def test_that_I_try_to_add_a_new_student_with_an_already_existing_username_throws_error(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        with self.assertRaises(ValueError) as context:self.student_management.add_student("chris101","daniel",19,"samuel123@gmail.com")
        self.assertEqual(str(context.exception), "Student already exists")
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

    def test_that_I_try_to_add_a_new_student_with_an_invalid_age_throws_error(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        with self.assertRaises(ValueError) as context:self.student_management.add_student("boss","Aminu",45,"aminu101@gmail.com")
        self.assertEqual(str(context.exception), "Age must be between 0 and 30")
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)


    def test_that_I_try_to_add_a_new_student_with_an_invalid_email_throws_error(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        with self.assertRaises(ValueError) as context:self.student_management.add_student("idanski","Papa",20,"pap.com")
        self.assertEqual(str(context.exception), "Invalid Email Address")
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

    def test_that_I_add_a_new_student_I_can_enroll_him_to_a_course(self):
        courses = self.student_management.get_student_courses("chris101")
        self.assertEqual(courses, [])

        self.student_management.enroll_student("chris101","Math")
        courses = self.student_management.get_student_courses("chris101")
        self.assertEqual(courses, ["Math"])

    def test_that_I_try_to_enroll_a_student_without_adding_him_throws_an_error(self):
        with self.assertRaises(ValueError) as context:self.student_management.enroll_student("lamine","Math")
        self.assertEqual(str(context.exception), "Student does not exist")

    def test_that_I_add_a_new_student__and_I_try_to_enroll_him_to_a_course_twice_it_throws_an_error(self):
        courses = self.student_management.get_student_courses("chris101")
        self.assertEqual(courses, [])

        self.student_management.enroll_student("chris101","Math")
        with self.assertRaises(ValueError) as context: self.student_management.enroll_student("chris101","Math")
        self.assertEqual(str(context.exception), "Student already enrolled in this course")
        courses = self.student_management.get_student_courses("chris101")
        self.assertEqual(courses, ["Math"])

    def test_that_I_create_a_student_I_can_update_his_details(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        self.student_management.update_student("chris101","Samuel",20,"christian123@gmail.com")
        student = self.student_management.get_student("chris101")
        self.assertEqual(student.get_name(), "Samuel")
        self.assertEqual(student.get_age(), 20)
        self.assertEqual(student.get_email(), "christian123@gmail.com")

    def test_that_I_try_to_update_a_nonexistent_student_it_throws_an_error(self):
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

        with self.assertRaises(ValueError) as context:self.student_management.update_student("fade",19,"sade@gmail.com")
        self.assertEqual(str(context.exception), "Student does not exist")
        total_students = self.student_management.get_total_students()
        self.assertEqual(total_students, 1)

    def test_that_I_create_a_student_and_I_try_to_update_student_with_wrong_email_it_throws_an_error(self):
        student = self.student_management.get_student("chris101")
        self.assertEqual(student.get_name(), "Christian")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_email(), "samuelchristian769@gmail.com")

        with self.assertRaises(ValueError) as context:self.student_management.update_student("chris101","sammy",18,"sammy9")
        self.assertEqual(str(context.exception), "Invalid Email Address")
        self.assertEqual(student.get_name(), "Christian")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_email(), "samuelchristian769@gmail.com")

    def test_that_I_create_a_student_and_I_try_to_update_student_with_invalid_age_it_throws_an_error(self):
        student = self.student_management.get_student("chris101")
        self.assertEqual(student.get_name(), "Christian")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_email(), "samuelchristian769@gmail.com")

        with self.assertRaises(ValueError) as context:self.student_management.update_student("chris101","sammy",70,"sammy9")
        self.assertEqual(str(context.exception), "Age must be between 0 and 30")
        self.assertEqual(student.get_name(), "Christian")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_email(), "samuelchristian769@gmail.com")

    def test_that_I_create_a_student_I_can_update_only_name_and_my_other_details_remain_same(self):
        student = self.student_management.get_student("chris101")
        self.assertEqual(student.get_name(), "Christian")
        self.assertEqual(student.get_age(), 18)
        self.assertEqual(student.get_email(), "samuelchristian769@gmail.com")

        self.student_management.update_student("chris101","sammy")





if __name__ == '__main__':
    unittest.main()
