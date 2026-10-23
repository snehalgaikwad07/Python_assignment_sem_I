#Q13. Check whether the number is palindrome.
num=int(input("Enter a number:"))
org_num=num
rev=0
while org_num!=0:
    digit=org_num%10
    rev=rev*10+digit
    org_num=org_num//10
if rev==num:
    print("number is palindrome.")
else:
    print("number is not palindrome.")