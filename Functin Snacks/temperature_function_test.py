import unittest
import temperature_function

class TestMinutes(unittest.TestCase):
    def test_that_temp_checker_exists(self):
        temperature_function.temp_checker(130,"C",17)
    def test_that_temp_checker_returns_correct_value(self):
        actual = temperature_function.temp_checker(130,'C',15)
        expected = "Heat alert"
        self.assertEqual(actual,expected)
        actual = temperature_function.temp_checker(1300,"F",1200)
        expected = "Heat alert"
        self.assertEqual(actual,expected)
    def test_that_temp_checker_of_raises_type_error_for_non_integers(self):
        self.assertRaises(TypeError, temperature_function.temp_checker, "sam", 7)
