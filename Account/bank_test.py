import unittest
from bank import Bank


class BankTest(unittest.TestCase):

    def setUp(self):
        self.chris_bank = Bank("Chris Bank")
        self.chris_bank.create_account("1234", "Christian", "07014570442")

    def test_that_create_account_and_deposit_5k_balance_is_5k(self):

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(0, balance)

        self.chris_bank.deposit("7014570442", 5000)

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(5000, balance)

    def test_that_invalid_account_number_deposit_throws_exception(self):

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(0, balance)

        with self.assertRaises(ValueError):
            self.chris_bank.deposit("70145704", 5000)

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(0, balance)

    def test_that_creating_account_with_invalid_pin_throws_exception(self):

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

        with self.assertRaises(ValueError):
            self.chris_bank.create_account("1888234", "Chris Bank", "07014570442")

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

    def test_that_creating_account_with_invalid_phone_number_throws_exception(self):

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

        with self.assertRaises(ValueError):
            self.chris_bank.create_account("1234", "Chris Bank", "0701457094")

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

    def test_that_duplicate_account_creation_throws_exception(self):

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

        with self.assertRaises(ValueError):
            self.chris_bank.create_account("1234", "Christian", "07014570442")

        number_of_accounts = self.chris_bank.get_number_of_accounts()
        self.assertEqual(1, number_of_accounts)

    def test_that_deposit_5k_and_withdraw_2k_balance_is_3k(self):

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(0, balance)

        self.chris_bank.deposit("7014570442", 5000)
        self.chris_bank.withdraw("7014570442", 2000, "1234")

        balance = self.chris_bank.check_balance("7014570442", "1234")
        self.assertEqual(3000, balance)


if __name__ == "__main__":
    unittest.main()