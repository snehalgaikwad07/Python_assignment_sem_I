#    ************************************TEXT ANALYZER SYSTEM ***********************************


text = input("Enter a sentence or paragraph: ")

# Remove extra spaces
text = text.strip()

# Count characters and words
characters = len(text)
words = text.split()
total_words = len(words)

# Count sentences
sentences = text.count(".") + text.count("?") + text.count("!")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
special = 0

# Count vowels, consonants, digits and special characters
for ch in text:

    if ch.lower() in "aeiou":
        vowels = vowels + 1

    elif ch.isalpha():
        consonants = consonants + 1

    elif ch.isdigit():
        digits = digits + 1

    elif ch != " ":
        special = special + 1

# Display uppercase and lowercase
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())

# Search a word
search = input("\nEnter a word to search: ")

if search.lower() in text.lower().split():
    print("Word found!")
else:
    print("Word not found!")

# Find word frequency
print("\nWord Frequency:")

for word in words:
    count = 0

    for w in words:
        if word.lower() == w.lower():
            count = count + 1

    print(word, ":", count)

# Display final report
print("\n----- Text Analysis Report -----")

print("Total Characters:", characters)
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Total Digits:", digits)
print("Special Characters:", special)

print("\nText after removing extra spaces:")
print(text)
