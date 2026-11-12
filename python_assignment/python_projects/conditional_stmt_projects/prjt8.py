#*************** Movie Ticket Booking System ***********************

name=input("Enter your name:")
age=int(input("Enter your age:"))
show_type=input("Enter show type(Morning / Evening):")
day_type=input("Enter day type(weekday/weekend):")

ticket=200
discount=0
surcharge=0

if age>0:
    if age<=12:
        discount=100
    elif age>=60:
        discount=60

if show_type.lower()=="morning":
    discount=discount+30

if day_type.lower()=="weekend":
    surcharge=50

#calculating final ticket price
final_price=ticket-discount+surcharge

#Output :- details of customer

print("*******Movie Ticket Details********")
print("Customer Name:",name)
print("Original Ticket price:Rs.",ticket)
print("Discount:Rs.",discount)
print("Weekend Surcharge:Rs.",surcharge)
print("Final Ticket Price:Rs.",final_price)

