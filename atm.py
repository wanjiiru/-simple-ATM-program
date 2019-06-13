from timeit import default_timer as timer
import datetime
from atmclass import BankAccount
a = BankAccount(100000)

##main menu
def main_menu():

    print(""" What would you like to do?
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
    exit()

##deposit
elif Choice==3:
    print(" Your Balance is  KES ",a.get_balance())
    amount_to_deposit=float(input("Please enter amount to deposit:"))
    if amount_to_deposit>40000:
        print('please enter an amount upto 40000')
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











