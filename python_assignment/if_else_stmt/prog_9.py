#Q9. write a program to check whether a student has passed or failed (pass marks=40)
marks=int(input("Enter students marks:"))
if marks<40:
    print("you are Failed!")
elif marks>=40:
    print("Congrats you are passed in exam!")