#Q34. Write a program to check whether a year is a leap year and century year.
year=int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap and century year.")
        else:
            print(year,"is a century year but not leap year.")
    else:
        print(year,"is a leap year but not century year.")
else:
    print(year,"is not a leap year and not a century year.")

