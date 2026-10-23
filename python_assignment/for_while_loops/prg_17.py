#Q17. Find largest digit in a number.
num=int(input("Enter a number:"))
larger=0
while num!=0:
    digit=num%10
    if digit>larger:
       larger=digit
    num=num//10
print("larger digit in number:",larger)