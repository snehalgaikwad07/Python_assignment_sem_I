#Q38. Find smallest digit in a number.
num=int(input("Enter a number:"))
small=9
while num>0:
      digit=num%10
      if digit<small:
         small=digit
      num=num//10
print(small)
