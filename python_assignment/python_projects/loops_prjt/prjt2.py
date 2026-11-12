#*************** Student marks and grade report ********************
n=int(input("Enter number of students:"))
total=0
pass_count=0
fail_count=0

for i in range(1,n+1):
    print("Enter Details of student:")
    name=input("Enter students name:")
    marks=float(input("Enter your marks:"))
    