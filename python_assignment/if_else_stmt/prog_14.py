#Q14. write a program to check whether a given character is uppercase or lowercase.
ch=input("Enter a character:")
if ch.islower():
    print(ch," is in lowercase!")
elif ch.isupper():
     print(ch," is in uppercase!")
else:
    print(ch," is not an alphabet!")