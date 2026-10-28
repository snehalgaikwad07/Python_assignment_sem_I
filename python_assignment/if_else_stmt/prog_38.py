#Q38. Write a program to check whether a student passed all subjects.
marks1=float(input("Enter marks of subject 1:"))
marks2=float(input("Enter marks of subject 2:"))
marks3=float(input("Enter marks of subject 3:"))
if marks1>=40 and marks2>=40 and marks3>=40:
    print("Student has passed all subjects.")
else:
    print("Student has not passed all subjects.")