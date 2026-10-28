#Q36. Find sum of numbers entered by user until 0 is entered.

sum=0
while True:
    num=int(input("Enter a number:"))
    if num==0:
        break
    else:
        sum=sum+num
print("Sum :",sum)