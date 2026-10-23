#Q23. write a program to calculate electricity bill based on units consumed.
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Electricity bill is Rs.", bill)