class BankAccount:
    """A bank account class"""
    def __init__(self, balance=100000):

        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self.balance

    def withdrawal(self, amount, limit=50000):
        if self.balance - amount > 0 and amount <= limit:
            self.balance -= amount
            return self.balance
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

##going back to main menu
def go_back_to_main_menu():
    what_to_do_next = input('Type “menu” and press enter to go back to main menu : ')
    main_menu()


Choice =int(input("Enter Option: "))

if Choice==1:
        print(" Your Balance is  KES ",a.get_balance())

elif Choice==2:
    print('\n')
    print(" Your Balance is  KES ",a.get_balance())
    withdraw_amount=float(input("Please enter amount to withdraw:"))
    new_balance=a.withdrawal(withdraw_amount)
    print("Your balance is   kes ", int(float(new_balance)))
    go_back_to_main_menu()

elif Choice==3:
    print(" Your Balance is  KES ",a.get_balance())
    amount_to_deposit=float(input("Please enter amount to deposit:"))
    if amount_to_deposit>150000:
        print('please enter an amount below 1500000')
        go_back_to_main_menu()
    else:
        new_balance=a.deposit(int(amount_to_deposit))
        print("Your balance is   kes ", new_balance)
        go_back_to_main_menu()

elif Choice==4:
        ask=str(input("""
        Are you sure you want to exit
        """))

        if ask in  ['yes', 'y','yeah'] :
            exit()
        else:
            main_menu()











