#Q35. Print multiplication tables from 1 to 5.
num=int(input("Enter a number:"))
print("Multiplication table of:",num)
for i in range(1,11,1):
    table=num*i
    print(table)