#**********  Student Scholarship Eligibility ***************
name=input("Enter Students Name:")
percentage=float(input("Enter your last year percentage:"))
annual_income=float(input("Enter your annual family income:"))
attendance_percentage=float(input("Enter your attendance percentage:"))

if percentage>=75 :
       if annual_income<=400000:
           if attendance_percentage>=75:
                if percentage>=90:
                  print("Full Scholarship!")
                else:
                 print("Partial Scholarship!")

           else:
              print("Not eligible for scholarship!") 
              print("Reason: Attendance is below 75%")
       else:
           print("Not eligible for scholarship!")
           print("Reason:Annual family income is more than Rs. 400000")
else:
    print("Not eligible for scholarship!")
    print("Reason:Percentage is below 75%")