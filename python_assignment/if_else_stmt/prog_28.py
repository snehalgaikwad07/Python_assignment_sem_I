#28. Write a program to calculate discounts based on total shopping amount.
total_amount=float(input("Enter total shopping amount:"))
if total_amount>=1000:
    discount=total_amount*0.1
    print("Discount Rs.",discount)
else:
    print("No discount applicable")