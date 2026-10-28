#Q33. Print reverse of a string.
str=input("Enter a string:")
rev=""
for i in str:
    rev=i+rev
print(rev)