class BankAccount:
    """A bank account class"""
    def __init__(self, balance=100000):

        self.balance = int(balance)

    def get_balance(self):
        return self.balance

    def deposit(self, amount,limit=40000):
        trx_amount_per_day=0
        self.balance += amount
        trx_amount_per_day=self.balance
        return self.balance

    def withdrawal(self, amount, limit=20000):
        withdrawal_frequency=0
        if self.balance - int(amount) > 0 and int(amount) <= limit:
            self.balance -= int(amount)
            withdrawal_frequency=+1
            return self.balance
        else:
             raise ValueError( 'Your withdrawal amount is {} which exceeds the transaction limit ! You have:' \
                   '\n{}. Your withdrawal limit is {}'.format(amount, self.balance, limit))

#bank account object
a = BankAccount(100000)