import unittest


class TestUser(unittest.TestCase):
    @classmethod
    def SetupUserClass(cls):
        '''
                set up structure before every test
                '''
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        print("teardown class")

    def setUp(self):
        '''
        clean up after running each test
        '''
        from atmclass import BankAccount
        self.customerA = BankAccount(balance=1000000)

    def test_initialization(self):
        '''
        Test for case initialization
        this methods checks whether instantiation is done well
        '''
        self.assertEqual(self.customerA.get_balance(), 1000000)

    def test_that_icannot_withdraw_amount_greaterthan_my_balance(self):
        '''
        this method checks if an error is raised if user tries to withdraw an amount greater than their balance
        :return:
        '''
        with self.assertRaises(ValueError):
            self.customerA.withdrawal(100000000)

    def test_withdraw_20000(self):
        '''
        This method tests a normal successful withdrawal
        :return:
        '''
        self.assertEqual(self.customerA.withdrawal(20000), int(980000))
    def test_deposit_10000(self):
        '''
        test a normal successful deposit
        :return:
        '''
        self.assertEqual(self.customerA.deposit(10000),1010000)

    def test_depositing_of_1_milliontoexistingamount(self):
        '''
        This method tests to check whether a use can deposit an amount greater than the transaction amount

        :return:
        '''
        self.assertRaises(ValueError)
        self.customerA.deposit(1000000)


    def tearDown(self):
        pass

if __name__ == '__main__':
    print("testing")
    unittest.main()
