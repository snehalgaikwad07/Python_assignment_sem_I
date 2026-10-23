#Q7. Calculate factorial of number using for loop.
num=int(input("Enter number for factorial:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("FACTORIAL OF ",num," is: ",fact)