#Q11. Count number of digit in given number.
num=int(input("Enter a number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("Number of digit is: ",count)