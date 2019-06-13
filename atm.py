balance = 100000
print("    ATM    ")


print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit


""")


def withdraw(balance,amount,max_per_transaction=20000):
    if balance<0:
        balance=balance-10
    else:
        balance=balance-amount
    return balance

def deposit(balance, amount):
    if amount>40000:
        print('enter right amount')
    else:
        balance=+amount



Choice =int(input("Enter Option: "))

if Choice==1:
    print(" Your Balance is  KES ",balance)

if Choice==2:
    print(" Your Balance is  KES ",balance)
    withdraw_amount=float(input("Please enter amount to withdraw "))

    if withdraw_amount>20000:
        print('Maximum amount per transaction is 20000')

    elif withdraw_amount>1 and withdraw_amount<balance:
        amount_remaining=withdraw(balance,amount=withdraw_amount)
        print("Your balance is   kes ",amount_remaining)
        exit()

    elif withdraw_amount>balance:
        print("Not enough funds in your account")
        exit()

elif Choice==3:
    print(" Your Balance is  KES ", balance)
    deposit_amount = float(input("Enter amount to deposit "))
    if deposit_amount>1 and deposit_amount<40000:
        new_balance=(balance+deposit_amount)
        print("Your balance is   kes ",new_balance)
    else:
        print('Please enter an amount between 1 and 50000')



elif Choice==4:
    options=[1,2]
    ask=input("""
    are you sure you want to exit
    """)
    if ask ==1 or 'yes':
        exit()

