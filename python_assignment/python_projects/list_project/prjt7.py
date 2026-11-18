#******************* # Payroll Processing Pipeline ******************

from functools import reduce
from operator import add

emp = [
    ["Amit", 20000, 5000, 2000, "ABCDE1234F"],
    ["Sneha", 30000, 7000, 3000, "FGHIJ5678K"],
    ["Rahul", 15000, 3000, 2000, "LMNOP1234Q"],
    ["Priya", 40000, 8000, 4000, "RSTUV5678W"]
]

gross = list(map(lambda x: x[1] + x[2] + x[3], emp))

bonus = list(filter(lambda x: x[1] >= 25000, emp))

net = []

for i in range(len(emp)):
    b = 2000 if emp[i][1] >= 25000 else 0
    t = gross[i] * 0.10
    net.append(gross[i] - t + b)

total = reduce(add, net)

pay = list(zip(map(lambda x: x[0], emp), net))

tax = any(map(lambda x: x > 30000, gross))

pan = all(map(lambda x: len(x[4]) == 10, emp))

print("\n------ PAYROLL REGISTER ------")

print("Name\tGross Salary\tNet Salary")

for i in range(len(emp)):
    print(emp[i][0], "\t", gross[i], "\t\t", round(net[i], 2))

print("\nBonus Eligible Employees:")

for i in bonus:
    print(i[0])

print("\nTotal Salary Disbursement: Rs.", round(total, 2))

print("Any employee exceeds tax slab:", tax)
print("All employees have valid PAN length:", pan)