# Random-dict-words: Read from a text file, select a random set of words from the file, and put those words together into a "sentence".

file = open("words")

# variable to store the dictionary words.
word_list = []

for word in file:
  word_list.append(word)

print(word_list)