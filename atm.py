balance = 50.00
print("    ATM    ")


print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit


""")

Choice =int(input("Enter Option: "))

if Choice==1:
    print(" Your Balance is  KES ",balance)

if Choice==2:
    print(" Your Balance is  KES ",balance)
    withdraw_amount=float(input("Please enter amount to withdraw "))
    if withdraw_amount>0 and withdraw_amount<balance:
        amount=(balance-withdraw_amount)
        print("Your balance is   kes ",amount)
    elif withdraw_amount>balance:
        print("Not enough funds in your account")

elif Choice==3:
    print(" Your Balance is  KES ", balance)
    deposit_amount = float(input("Enter amount to deposit "))
        if Deposit > 0:
            forewardbalance = (balance + Deposit)
            print("Forewardbalance  £ ", forewardbalance)
        else:
            print("None deposit made")

    if Option == 4:
        exit()


