#Q39. Count total words in a string.
str=input("Enter a string:")
count=1
for i in str:
    if i==" ":
       count=count+1
print("Total words:",count)