#Q6. check whether a string starts with a given substring.
str=input("Enter a string:")
sub_str=input("Enter a subtring:")
if str.startswith(sub_str):
    print("String is start with",sub_str)
else:
    print("String is not start with",sub_str)