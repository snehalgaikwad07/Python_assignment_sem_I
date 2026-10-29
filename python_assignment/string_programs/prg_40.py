#Q40. Count uppercase and lowercase letters separately.
str=input("Enter a string: ")
upper = 0
lower = 0

for i in str:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)