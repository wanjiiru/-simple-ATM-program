from timeit import default_timer as timer
import datetime
from atmclass import BankAccount
account = BankAccount(100000)

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
        print(" Your Balance is  KES ",account.get_balance())
#withdraw
elif Choice==2:
    print('\n')
    print(" Your Balance is  KES ",account.get_balance())
    try:

        withdraw_amount=int(input("Please enter amount to withdraw:"))
        if withdraw_amount>50000:
            print('Enter correct amount with yor limit of 50,000')
        else:

            new_balance=account.withdrawal(withdraw_amount)
            print("Your balance is   kes ", new_balance)
    except:
        import traceback
        traceback.print_exc()

##deposit
elif Choice==3:
    print(" Your Balance is  KES ",account.get_balance())
    amount_to_deposit=float(input("Please enter amount to deposit:"))
    if amount_to_deposit>40000:
        print('please enter an amount upto 40000')
        main_menu()
    else:
        new_balance=account.deposit(int(amount_to_deposit))
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











