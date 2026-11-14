#************************************* Password Strength Checker ******************************
password = input("Enter your password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special + 1

print("\nPassword Details:")
print("Length:", len(password))
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
print("Special characters:", special)

if len(password) < 8:
    print("\nPassword Strength: Weak")
elif upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("\nPassword Strength: Strong")
elif upper > 0 and lower > 0 and digit > 0:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Weak")
