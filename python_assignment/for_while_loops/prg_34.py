#Q34. Check whether a string is palindrome.
str=input("Enter a string:")
rev=""
for i in str:
    rev=i+rev
if rev==str:
    print(str," is palindrome!")
else:
    print(str," is not palindrome!")