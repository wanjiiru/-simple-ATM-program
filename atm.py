from timeit import default_timer as timer
import datetime

start=timer()
stop=timer()
xx=stop-start
print(xx)
class BankAccount:
    """A bank account class"""
    def __init__(self, balance=100000):

        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        trx_amount_per_day=0
        self.balance += amount
        trx_amount_per_day=self.balance
        return self.balance,trx_amount_per_day

    def withdrawal(self, amount, limit=50000):
        withdrawal_frequency=0
        if self.balance - int(amount) > 0 and int(amount) <= limit:
            self.balance -= int(amount)
            withdrawal_frequency=+1
            return self.balance,withdrawal_frequency

        else:
            return 'Your withdrawal amount is {} which exceeds your account limit! You have:' \
                   '\n{}. Your withdrawal limit is {}'.format(amount, self.balance, limit)


#bank account object
a = BankAccount(100000)


##main menu
def main_menu():

    print("""
    1)        Balance
    2)        Withdraw
    3)        Deposit
    4)        Quit


    """)
main_menu()

##user inpiut
Choice =int(input("Enter Option: "))
#check balance
if Choice==1:
        print(" Your Balance is  KES ",a.get_balance())
#withdraw
elif Choice==2:
    print('\n')
    print(" Your Balance is  KES ",a.get_balance())
    withdraw_amount=int(input("Please enter amount to withdraw:"))
    new_balance=a.withdrawal(withdraw_amount)
    print("Your balance is   kes ", new_balance)
    main_menu()
##deposit
elif Choice==3:
    print(" Your Balance is  KES ",a.get_balance())
    amount_to_deposit=float(input("Please enter amount to deposit:"))
    if amount_to_deposit>150000:
        print('please enter an amount below 1500000')
        main_menu()
    else:
        new_balance=a.deposit(int(amount_to_deposit))
        print("Your balance is   kes ", new_balance)
        main_menu()
##exit
elif Choice==4:
        ask=str(input("""
        Are you sure you want to exit
        """))

        if ask in  ['yes', 'y','yeah'] :
            exit()
        else:
            main_menu()











