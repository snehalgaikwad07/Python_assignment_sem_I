#Q19. Swap uppercase characters to lowercase and vice versa.
str=input("Enter a string:")
if str.isupper():
    print(str," after converting in lowercase is:",str.lower())
elif str.islower():
    print(str," after converting in uppercase is:",str.upper())
else:
    print(str," is invalid string!")
