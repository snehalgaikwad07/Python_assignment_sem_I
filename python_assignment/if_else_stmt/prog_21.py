#Q21. write a program to find smallest of three number.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))
if num1<num2 and num1<num3:
    print(num1," is smaller than ",num2,",",num3)
elif num2<num1 and num2<num3:
    print(num2," is smaller than ",num1,",",num3)
else:
    print(num3," is smaller than ",num1,",",num2)