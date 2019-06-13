import unittest


class TestUser(unittest.TestCase):
    @classmethod
    def SetupUserClass(cls):
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")

    def setUp(self):
        from atmclass import BankAccount
        self.customerA = BankAccount(balance=1000000)

    def test_initialization(self):
        """this methods checks whether instantiation is done well"""
        self.assertEqual(self.customerA.get_balance(), 1000000)

    def test_that_icannot_withdraw_amount_greaterthan_my_balance(self):
        with self.assertRaises(ValueError):
            self.customerA.withdrawal(100000000)

    def test_withdraw_50000(self):
        self.assertEqual(self.customerA.withdrawal(500000), 500000)

    def test_depositing_of_1_milliontoexistingamount(self):
        self.assertAlmostEqual(self.customerA.deposit(1000000), 1000000)

    def tearDown(self):
        pass

if __name__ == '__main__':
    print("testing")
    unittest.main()
