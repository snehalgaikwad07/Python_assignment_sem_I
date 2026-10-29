#Q37. Find the longest word in a sentence.
str = input("Enter a sentence: ")
words = str.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
