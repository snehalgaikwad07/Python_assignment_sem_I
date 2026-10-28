#Q45.Write a program to print menu-based food selection using match case.
print("Menu:")
print("1. Pizza")
print("2. Burger")
print("3. Pasta")
choice=int(input("Enter your choice (1-3):"))
match choice:
    case 1:
        print("You have selected Pizza.")
    case 2:
        print("You have selected Burger.")
    case 3:
        print("You have selected Pasta.")
    case _:
        print("Invalid choice!")