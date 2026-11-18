#**************** Dynamic Tax & Discount Calculator  ***************


cart = []

tax = {
    "food": lambda x: x * 0.05,
    "clothes": lambda x: x * 0.12,
    "electronics": lambda x: x * 0.18,
    "luxury": lambda x: x * 0.28
}

coupon = {
    "SAVE10": lambda x: x * 0.10,
    "SAVE20": lambda x: x * 0.20,
    "FESTIVE": lambda x: 100 if x >= 1000 else 0
}

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    cat = input("Enter category (food/clothes/electronics/luxury): ").lower()
    price = float(input("Enter item price: "))

    cart.append([name, cat, price])

code = input("Enter coupon code: ").upper()

total = 0
tax_total = 0

print("---------- BILL ----------")

for i in cart:
    name = i[0]
    cat = i[1]
    price = i[2]

    if cat in tax:
        t = tax[cat](price)
    else:
        t = 0

    amt = price + t
    total = total + price
    tax_total = tax_total + t

    print("\nItem:", name)
    print("Category:", cat)
    print("Price: ₹", price)
    print("Tax: ₹", round(t, 2))
    print("Total: ₹", round(amt, 2))

print("Subtotal: ₹", round(total, 2))
print("Total GST: ₹", round(tax_total, 2))

discount = 0

if code in coupon:
    discount = coupon[code](total)
    print("Coupon Applied:", code)
else:
    print("Invalid coupon code!")

bill = total + tax_total - discount

print("Discount: ₹", round(discount, 2))
print("--------------------------")
print("Grand Total: ₹", round(bill, 2))
print("--------------------------")