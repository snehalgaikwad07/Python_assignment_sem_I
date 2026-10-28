#Q39. Write a program to check whether a number is greater than 0 and less than 100.
number=int(input("Enter a number:"))
if number>=0 and number<=100:
    print(number,"is greater than 0 and less than 100.")
else:
    print(number,"is not greater than 0 and less than 100.")