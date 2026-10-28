#Q24. Count vowels in a string.
str=input("Enter a string:")
count=0
for i in str:
    if i in "aiueoAUIOE":
       count=count+1
print("Number of vowels:",count)