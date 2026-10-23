#Q7. check whether a string ends with a given substring.
str=input("Enter a string:")
sub_str=input("Enter a substring:")
if str.endswith(sub_str):
    print("String ends with",sub_str)
else:
    print("String is not ends with",sub_str)