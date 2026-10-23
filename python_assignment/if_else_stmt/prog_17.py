#Q17. write a program to check grade based on marks(A,B,C,Fail).
marks=int(input("Enter your marks:"))
if marks>=0 and marks<=34:
    print("Failed!")
elif marks>35 and marks<=50:
    print("Your grade=C")
elif marks>=51 and marks<=80:
    print("Your grade=B")
elif marks>=81 and marks<=100:
    print("Your grade:A")
else:
    print("Invalid marks,please enter valid marks between(1-100)!")