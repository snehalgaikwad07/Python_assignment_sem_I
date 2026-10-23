#Q20. write a program to check ticket price based on age.
age=int(input("Enter your age:"))
if age>0 and age<=6:
    print("Free ticket")
elif age>=7 and age<=14:
    print("Price of ticket=20Rs.")
elif age>=15 and age<=18:
    print("Price of ticket=30Rs.")
elif age>=19 and age<=70:
    print("Price of ticket=50Rs.")
elif age>=71 and age<=100:
    print("Price of ticket=35Rs.")