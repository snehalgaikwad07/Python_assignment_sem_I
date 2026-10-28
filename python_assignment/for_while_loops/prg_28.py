#Q28. Check whether a number is Armstrong.
num=int(input("Enter a number:"))
sum=0
while  num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")