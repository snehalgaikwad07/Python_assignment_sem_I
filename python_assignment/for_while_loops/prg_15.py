#Q15. Find sum of digit of numbers.
num=int(input("Enter a number:"))
total=0
while num!=0:
    digit=num%10
    total+=digit
    num=num//10
print("Addition of digit:",total)