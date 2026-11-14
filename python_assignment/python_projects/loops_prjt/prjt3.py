
#******** ATM PIN Verification ********

sample_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    pin = input("Enter your ATM PIN: ")
    attempts = attempts + 1

    if pin == sample_pin:
        print("\nAccess Granted!")
        break

    else:
        print("Incorrect PIN!")

        if attempts < max_attempts:
            print("Attempts remaining:", max_attempts - attempts)

        else:
            print("Card Temporarily Locked!")

print("\n----- ATM Status -----")
print("Attempts Used:", attempts)

if attempts == max_attempts and pin != sample_pin:
    print("Access Status: Card Locked")
else:
    print("Access Status: Successful")
