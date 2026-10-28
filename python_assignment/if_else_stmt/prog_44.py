#Q44.Write a program to check traffic signal actions using match case.
signal=input("Enter traffic signal color (red, yellow, green):")
match signal:
    case 'red':
        print("Stop the vehicle.")
    case 'yellow':
        print("Prepare to stop the vehicle.")
    case 'green':
        print("Proceed with caution.")
    case _:
        print("Invalid signal color!")