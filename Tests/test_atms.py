import unittest

class BankAccount:

    def __init__(self):
        self.balance = 0.0

    def deposit_funds(self, amount):
        try:
            self.balance += amount
        except TypeError:
            raise TypeError

    def withdraw_funds(self, amount):
        balance=0.0
        if amount <= balance:
            self.balance -= amount



class TestBankAcount(unittest.TestCase):

    def setUp(self):
        self.test_account = BankAccount()
        self.test_account.balance = 1000

    def test_normal_deposit(self):
        expected_balance = 1100.0
        self.test_account.deposit_funds(100.0)
        self.assertEqual(expected_balance, self.test_account.balance)
        self.assertIsNotNone(self,expected_balance)

    def test_max_amount_raises_erroe(self):
        #  test wrong data type value
        with self.assertRaises(TypeError):
            self.test_account.deposit_funds('enter a number')

if __name__ == '__main__':

    unittest.main()