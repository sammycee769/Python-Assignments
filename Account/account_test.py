import unittest
from account import Account
# import account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(1234)


    def test_that_deposit_5k_with_valid_pin_gives_balance_5k(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 5000)

    def test_that_deposit_5k_with_valid_pin_twice_gives_balance_10k(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        self.account.deposit(5000)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 10000)

    def test_that_negative_deposit_with_valid_pin_does_not_change_balance(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(-5000)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)
        
    def test_that_deposit_5k_and_withdraw_2k_with_valid_pin_gives_balance_3k(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        self.account.withdraw(2000, 1234)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 3000)

    def test_that_withdraw_more_than_balance_with_valid_pin_does_not_change_balance(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        self.account.withdraw(6000, 1234)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 5000)

    def test_that_negative_withdraw_with_valid_pin_does_not_change_balance(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        self.account.withdraw(-2000, 1234)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 5000)

    def test_that_withdraw_exact_balance_with_valid_pin_gives_zero_balance(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

        self.account.deposit(5000)
        self.account.withdraw(5000, 1234)
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)

    def test_that_check_balance_with_invalid_pin_returns_invalid_pin_message(self):
        balance = self.account.check_balance(0000)
        self.assertEqual(balance, "Invalid PIN")
    
    def test_that_withdraw_with_invalid_pin_returns_invalid_pin_message(self):
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 0)
        
        self.account.deposit(5000)
        result = self.account.withdraw(2000, 0000)
        self.assertEqual(result, "Invalid PIN or insufficient funds")
        balance = self.account.check_balance(1234)
        self.assertEqual(balance, 5000)

    def test_that_validate_pin_returns_true_for_correct_pin(self):
        self.assertTrue(self.account.validate_pin(1234))

if __name__ == '__main__':
    unittest.main()