#Q42. Write a program to perform calculator operations using match case.
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter operation(+,-.*,/):")
match choice:
    case '+':
        print("Addition of",num1,"+",num2,":",num1+num2)
    case '-':
        print("Subtraction of",num1,"-",num2,":",num1-num2)
    case '*':
        print("Multiplication of",num1,"*",num2,":",num1*num2)
    case '/':
        print("Division of",num1,"/",num2,":",num1/num2)
    case _:
        print("Invalid operation!")