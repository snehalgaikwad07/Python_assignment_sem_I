#Q4. count the number of vowels in string.
str=input("Enter a string:")
count=0
for i in str:
    if i in "aeiouAEIOU":
        count+=1
print("Number of vowels in string:",count)