#Q28.Count the number of words in a sentence.
str=input("Enter a sentence:")
count=1
for i in str:
    if i==" ":
       count=count+1
print("Total number of words in this sentence:",count)