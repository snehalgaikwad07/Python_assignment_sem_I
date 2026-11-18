#*****************Real-time Stock Price Alert Filter *****************

stocks = [
    ("TCS", 4200.50, 3.5),
    ("INFY", 1450.75, 2.2),
    ("RELIANCE", 2800.00, -1.5),
    ("HDFC", 650.50, 4.2),
    ("WIPRO", 450.25, -2.5)
]

rules = []

print("1. Change greater than")
print("2. Price less than")

n = int(input("Enter number of alert rules: "))

for i in range(n):
    ch = int(input("Enter rule choice (1 or 2): "))
    val = float(input("Enter value: "))

    if ch == 1:
        rules.append(lambda x, v=val: x[2] > v)

    elif ch == 2:
        rules.append(lambda x, v=val: x[1] < v)

    else:
        print("Invalid rule!")

print("*** Stock Price Alert Report ***")

for i in range(len(rules)):
    result = list(filter(rules[i], stocks))

    print("Alert Rule", i + 1)

    if len(result) > 0:
        for s in result:
            price = list(map(lambda x: "₹" + format(x[1], ".2f"), [s]))
            print(s[0], "-", price[0], "-", s[2], "%")
    else:
        print("No matching stocks!")

print("*** All Stock Prices ***")

price = list(map(lambda x: x[0] + " : ₹" + format(x[1], ".2f"), stocks))

for i in price:
    print(i)