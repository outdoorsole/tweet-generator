# Random-dict-words: Read from a text file, select a random set of words from the file, and put those words together into a "sentence".

# Reads a file and generates a word list.
def create_word_list():
  file = open("words")

  # variable to store the dictionary words.
  word_list = []

  for word in file:
    word_list.append(word)

  return(word_list)

if __name__ == '__main__':
  dictionary_list = create_word_list()
  print(dictionary_list)