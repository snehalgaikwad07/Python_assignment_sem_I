#Q23. check whether a string is a palindrome.
str=input("Enter a string:")
if str==str[::-1]:
    print(str," is a palindrome string.")
else:
    print(str," is not a palindrome string.")