#Q13. write a program to check whether a number is zero or non-zero.
num=int(input("Enter a number:"))
if num<0 or num>0:
    print(num," is non-zero!")
elif num==0:
    print(num," is zero!")