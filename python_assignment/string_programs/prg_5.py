#Q5. count the number of consonants in a string.
str=input("Enter a string:")
count=0
for i in str:
    if i not in "aeiouAEIUE":
        count=count+1
print("Number of consotants present in string:",count)    