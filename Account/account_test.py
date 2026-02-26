import unittest
from account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.pension_account = Account("1234", "Christian", "07014570442")

    def test_that_deposit_5k_gives_5k_balance(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(5000, balance)

    def test_that_deposit_5k_again_gives_10k_balance(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)
        self.pension_account.deposit(5000)

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(10000, balance)

    def test_that_negative_deposit_throws_exception_and_balance_remains(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)

        with self.assertRaises(ValueError):
            self.pension_account.deposit(-5000)

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(5000, balance)

    def test_that_deposit_and_withdraw_gives_correct_balance(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)
        self.pension_account.withdraw(5000, "1234")

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

    def test_that_negative_withdraw_throws_exception_and_balance_remains(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)

        with self.assertRaises(ValueError):
            self.pension_account.withdraw(-5000, "1234")

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(5000, balance)

    def test_that_withdraw_more_than_balance_throws_exception(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)

        with self.assertRaises(ValueError):
            self.pension_account.withdraw(15000, "1234")

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(5000, balance)

    def test_that_check_balance_with_invalid_pin_throws_exception(self):
        with self.assertRaises(ValueError):
            self.pension_account.check_balance("0000")

    def test_that_withdraw_with_invalid_pin_throws_exception_and_balance_remains(self):
        balance = self.pension_account.check_balance("1234")
        self.assertEqual(0, balance)

        self.pension_account.deposit(5000)

        with self.assertRaises(ValueError):
            self.pension_account.withdraw(5000, "0000")

        balance = self.pension_account.check_balance("1234")
        self.assertEqual(5000, balance)

    def test_that_creating_account_with_invalid_phone_number_throws_exception(self):
        with self.assertRaises(ValueError):
            Account("1234", "Samuel", "070145702")


if __name__ == "__main__":
    unittest.main()