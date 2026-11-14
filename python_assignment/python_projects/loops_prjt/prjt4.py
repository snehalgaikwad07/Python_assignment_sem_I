
#******** Shopping Cart Total ********

n = int(input("Enter number of products: "))

subtotal = 0

for i in range(1, n + 1):

    print("\nEnter details of Product", i)

    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if price >= 0 and quantity >= 0:

        item_total = price * quantity

        print("Item Subtotal: Rs.", item_total)

        subtotal = subtotal + item_total

    else:
        print("Invalid price or quantity!")


discount = 0

if subtotal >= 3000:
    discount = subtotal * 10 / 100


discounted_amount = subtotal - discount


if discounted_amount < 1500:
    delivery = 100
else:
    delivery = 0

# Calculate final amount
final_amount = discounted_amount + delivery

# Display 
print("\n----- Shopping Cart Bill -----")
print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", discount)
print("Delivery Charge: Rs.", delivery)
print("Final Payable Amount: Rs.", final_amount)
