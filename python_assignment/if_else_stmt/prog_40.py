#Q40. Write a program to check whether a password is valid using nested if.
password=input("Enter a password:")
if len(password)>=8:
    if any(char.isdigit()for char in password):
        if any(char.isupper() for char in password):
            print("Password is valid.")
else:
    print("Password is invalid.")