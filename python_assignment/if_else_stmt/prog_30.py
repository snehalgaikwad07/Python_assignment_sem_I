#Q30. Write a program to check the type of number (single, double, or three digit).
number=int(input("Enter a number:"))
if number>=0 and number<=9:
    print("Single digit number.")
elif number>=10 and number<=99:
    print("Double digit number.")
else:
    print("Three digit number.")