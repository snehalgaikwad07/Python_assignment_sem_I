#****************Grocery Shopping Cart Manager *******************


cart = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Update quantity")
    print("4. View cart")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        cart.append([item, qty, price])
        print("Item added successfully!")

    elif ch == 2:
        item = input("Enter item name to remove: ")

        for i in cart:
            if i[0] == item:
                cart.remove(i)
                print("Item removed!")
                break
        else:
            print("Item not found!")

    elif ch == 3:
        item = input("Enter item name: ")

        for i in cart:
            if i[0] == item:
                qty = int(input("Enter new quantity: "))
                i[1] = qty
                print("Quantity updated!")
                break
        else:
            print("Item not found!")

    elif ch == 4:
        print("\n--- Shopping Cart ---")

        total = 0
        lst = []

        for i in cart:
            cost = i[1] * i[2]
            total = total + cost
            lst.append([i[0], cost])

            print(i[0], "-", i[1], "x", i[2], "=", cost)

        discount = 0

        if total >= 1000:
            discount = total * 0.10

        bill = total - discount

        print("Subtotal:", total)
        print("Discount:", discount)
        print("Grand Total:", bill)

        lst = sorted(lst, key=lambda x: x[1], reverse=True)

        print("\nTop 3 Expensive Items:")
        print(lst[:3])

    elif ch == 5:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")