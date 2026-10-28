#Q24. Count consonants in a string.
str=input("Enter a string:")
count=0
for i in str:
    if i not in "aeiouAEIOU":
        count=count+1
print("Number of consonants:",count)