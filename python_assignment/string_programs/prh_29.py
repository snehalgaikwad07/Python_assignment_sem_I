#Q29. Replace a word with another word in a sentence.
str = input("Enter a sentence: ")
word = input("Enter a word to replace: ")
replace_word = input("Enter replacement word: ")
str = str.replace(word, replace_word)
print("Updated sentence:", str)
