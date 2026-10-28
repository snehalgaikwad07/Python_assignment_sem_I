#Q50. Write a program to build a simple ATM menu using a match case.
print("******ATM Menu******")
print("1.Check balance")
print("2.Deposit money")
print("3.Withdraw Money")
print("4.Change PIN")
print("5.Exit")
choice=int(input("Enter your choice between(1-5):"))
match choice:
    case 1:
        print("You have selected to check balance!")
    case 2:
        print("You have selected to Deposit money!")
    case 3:
        print("You have selected to Withdraw money!")
    case 4:
        print("You have selected to Change PIN!")
    case 5:
        print("You have selected to Exit from menu!")
    case _:
        print("Invalid choice!")