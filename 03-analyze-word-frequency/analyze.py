# Analyze.py
# Performs Text Analysis on the frequency of words within a body of source text.

# Specifications:
# A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.

# A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

def generate_word_list():
  lines_array = []

  with open('words.txt', 'r') as file:
    data = file.read().split('\n')
    
    for line in data:
      words_list = line.split()
      lines_array += words_list
  print len(lines_array)
  return lines_array

def histogram(word_list):
  # returns a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
  print(word_list)
  print word_list.count(word_list[3])


def unique_words():
  print()

def frequency():
  print()

words = generate_word_list()
histogram(words)
print words