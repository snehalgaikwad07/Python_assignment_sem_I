#Q38. Find the shortest word in a sentence.
str = input("Enter a sentence: ")
words = str.split()
shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i

print("Shortest word:", shortest)
