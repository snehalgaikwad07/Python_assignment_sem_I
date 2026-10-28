#Q32. Calculate power of a number without using pow().
num=int(input("Enter a number:"))
exp=int(input("Enter exponent:"))
result=1
for i in range(exp):
    result=result*num
print(result)