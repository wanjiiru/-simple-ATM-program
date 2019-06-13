import unittest
from atm import BankAccount


class TestUser(unittest.TestCase):
    @classmethod
    def SetupUserClass(cls):
        """This method is a life cycle hook for this class"""
        print("setup class")

    @classmethod
    def tearDownClass(cls):
        """this method is executed after each test"""
        print("teardown class")

    def setUp(self):
        """
    This method sets up the data needed to test User class"""
        self.customerA = BankAccount(balance=1000000)

    def test_init(self):
        """this methods checks whether instantiation is done well"""
        self.assertEqual(self.customerA.get_balance(), 1000000)

    def tearDown(self):
        """ run to clean up the class"""


if __name__ == '_main_':
    print("testing")
    unittest.main()
