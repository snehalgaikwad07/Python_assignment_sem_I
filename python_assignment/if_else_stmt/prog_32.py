#Q32.Write a program to check whether a student is eligible for an exam (attendance + marks).
attendance=float(input("Enter attenddance percentage:"))
marks=float(input("Enter marks percentage:"))
if attendance>=75 and marks>=40:
    print("Student is eligible for the exam.")
else:
    print("Student is not eligible for the exam.")