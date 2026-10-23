#Q22. write a program to check salary bonus based on years of service.
year_service=int(input("Enter your years of service:"))
if year_service>0 and year_service<=2:
    print("Salary bonus=20000")
elif year_service>=3 and year_service<=5:
    print("Salary bonus=40000")
elif year_service>=6 and year_service<=8:
    print("Salary bonus=60000")
elif year_service>=9 and year_service<=10:
    print("Salary bonus=80000")