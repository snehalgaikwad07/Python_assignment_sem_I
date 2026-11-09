#***************** ATM Withdrawal System ****************
name=input("Enter your name:") 
balance=float(input("Enter the current balance:"))
withdrawal_amount=float(input("Enter the withdrawal amount:"))

print("\n----- ATM Transaction Details -----")
print("Account Holder:", name)

if withdrawal_amount>0:
    if withdrawal_amount<=balance and withdrawal_amount<=20000:
       balance=balance-withdrawal_amount

       print("Transaction Status: Successful")
       print("Withdrawn Amount: Rs.", withdrawal_amount)
       print("Remaining Balance: Rs.", balance)

       if balance<=1000:
          print("LOW ACCOUNT BALANCE!")
    else:
        if withdrawal_amount > balance and withdrawal_amount > 20000:
            print("Transaction Status: Rejected")
            print("Reason: Insufficient Balance and Exceeds Withdrawal Limit")

        elif withdrawal_amount > balance:
            print("Transaction Status: Rejected")
            print("Reason: Insufficient Balance")

        else:
            print("Transaction Status: Rejected")
            print("Reason: Maximum withdrawal limit is Rs. 20000")

else:
    print("Transaction Status: Rejected")
    print("Reason: Withdrawal amount must be greater than Rs. 0")


