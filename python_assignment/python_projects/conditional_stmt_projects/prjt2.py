#***********************Online Shopping Checkout ************************
name=input("Enter your name:")
amount=float(input("Enter the amount:"))
customer_type=input("Enter the customer type(premium/regular):")

discount=0
if amount>=5000:
    discount=20
elif amount>=3000 and amount<5000:
    discount=10
elif amount>=1000 and amount<3000:
    discount=5
else:
    discount=0

if customer_type.lower() == "premium":
    discount = discount + 5
elif customer_type.lower() == "regular":
    discount = discount

else:
    print("Invalid Customer Type!")
    
# Calculate discount amount
discount_amount = amount * discount / 100

# Calculate amount after discount
final_amount = amount - discount_amount

if final_amount>=2000:
    if final_amount>0:
        delivery=0
    else:
        delivery=100
else:
    delivery=100

print("******Checkout Details******")
print("Customer Name:",name)
print("Customer Type:",customer_type)
print("Amount:",amount)
print("Discount:",discount)
print("Delivery Charges:",delivery)
print("Final Amount to be paid:",final_amount+delivery)
    