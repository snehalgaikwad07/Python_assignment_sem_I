#Q27. Check whether a word exists in a sentence.
str=input("Enter a sentence:")
word=input("Enter a word:")
if word in str:
    print(word," is exists in sentence.")
else:
    print(word," is not exists in sentence.")