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
        expected = "cold advisory"
        self.assertEqual(actual,expected)
