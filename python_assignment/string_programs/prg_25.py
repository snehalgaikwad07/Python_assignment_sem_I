#Q25.Extract only alphabets from a string.
str=input("Enter a string:")
alphabet=""
for i in str:
    if i.isalpha():
        alphabet=alphabet+i
print("Extract only alphabet from ",str,":",alphabet)