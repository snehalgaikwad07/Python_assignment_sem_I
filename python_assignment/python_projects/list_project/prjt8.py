# **********************   Sales Data Aggregator for a Retail Chain   *************************

from functools import reduce

b1 = [50000, 60000, 45000, 70000, 55000]
b2 = [40000, 50000, 65000, 60000, 45000]
b3 = [30000, 45000, 50000, 55000, 60000]

branch = [b1, b2, b3]
name = ["Branch 1", "Branch 2", "Branch 3"]

total = list(map(sum, zip(b1, b2, b3)))

lakhs = list(map(lambda x: x / 100000, total))

monthly = list(map(sum, branch))

grand = reduce(lambda x, y: x + y, monthly)

max_sale = reduce(lambda x, y: x if x > y else y, total)

below = list(filter(lambda x: x < 150000, total))

rank = sorted(zip(name, monthly), key=lambda x: x[1], reverse=True)

print("------ BRANCH WISE SALES ------")

for i, b in enumerate(branch):
    print(i + 1, name[i], ":", sum(b))

print("------ DAY WISE TOTAL SALES ------")

for i, x in enumerate(total):
    print("Day", i + 1, ":", x)

print("------ SALES IN LAKHS ------")

for i, x in enumerate(lakhs):
    print("Day", i + 1, ":", round(x, 2), "Lakhs")

print("Monthly Sales:", grand)

print("Maximum Single Day Sale:", max_sale)

print("Days Below Target:")

for i in range(len(below)):
    print("Day", total.index(below[i]) + 1, ":", below[i])

print("------ BRANCH RANKING ------")

for i, b in enumerate(rank):
    print(i + 1, b[0], ":", b[1])