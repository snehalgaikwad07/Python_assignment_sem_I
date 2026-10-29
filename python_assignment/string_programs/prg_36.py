#Q36. Remove duplicate characters from a string.
str = input("Enter a string: ")
result = ""

for i in str:
    if i not in result:
        result += i

print(result)