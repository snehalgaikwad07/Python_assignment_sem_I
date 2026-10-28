#Q42. Calculate sum of squares of first n numbers.
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
   sum=sum+i*i
print("sum:",sum)