#Q3. Write a program to check whether a person is eligible to vote or not.
age=int(input("Enter your age:"))
if age<=18:
    print("User cannot vote!")
elif age>18:
    print("User can vote!")