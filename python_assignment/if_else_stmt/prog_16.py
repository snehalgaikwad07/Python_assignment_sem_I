#Q16. write a program to find the greatest of three numbers.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
if num1>num2 and num1>num3:
    print(num1," is greather than ",num2,",",num3)
elif num2>num1 and num2>num3:
    print(num2," is greater than ",num1,",",num3)
else:
    print(num3," is greater than ",num1,",",num2)
