#Q10. Find the index of a given character in a string.
str=input("Enter a string:")
char=input("Enter a character to find index:")

index=str.find(char)
if index!=-1:
    print("Inndex of ",char,"is:",str.index(char))
else:
    print(char,"is not present in given string ",str)
