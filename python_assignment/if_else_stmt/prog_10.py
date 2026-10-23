#Q10. write a program to check whether a given number is single digit or not
num_length=int(input("Enter number length:"))
num=int(input("Enter number:"))
if num_length<=1:
    print(num," is single digit!")
else:
    print(num," is not single digit!")