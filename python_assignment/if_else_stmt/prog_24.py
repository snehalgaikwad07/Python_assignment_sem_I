#Q24. write a program to check result(Distinction ,First Class,Pass,Fail)
marks=int(input("Enter your marks:"))
if marks>0 and marks<=34:
    print("Failed")
elif marks>=35 and marks<=70:
    print("Passed")
elif marks>=71 and marks<=80:
    print("First Class")
elif marks>=81 and marks<=100:
    print("Passed with Distinction.")
else:
    print("Invalid marks,Please enter correct marks.")