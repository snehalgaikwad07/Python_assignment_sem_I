#Q31. Remove punctuation marks from a string.
str = input("Enter a string: ")
result = ""

for i in str:
    if i.isalnum() or i == " ":
        result += i

print("String without punctuation:", result)