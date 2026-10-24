#Q24. Extract only digits from a string.
str=input("Enter a string:")
digits=""
for i in str:
    if i.isdigit():
        digits=digits+i
print("The digits from the string are:",digits)