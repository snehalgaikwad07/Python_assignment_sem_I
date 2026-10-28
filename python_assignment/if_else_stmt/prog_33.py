#Q33.Write a program to check whether a person can apply for a loan.
income=float(input("Enter your monthly income:"))
if income>=50000:
    print("You are eligible to apply for a loan.")
else:
    print("You are not eligible to apply for a loan.")