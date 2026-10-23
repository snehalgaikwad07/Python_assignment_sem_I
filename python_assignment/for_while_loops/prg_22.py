#Q22. Sum of even digit in number.
num=int(input("Enter a number:"))
sum=0
while num>0:
    digit=num%10
    if digit%2==0:
        sum=digit+sum 
    num=num//10
print("sum of even digit from number: ",sum)