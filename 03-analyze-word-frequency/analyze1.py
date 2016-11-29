# Analyze.py
# Performs Text Analysis on the frequency of words within a body of source text.

# Specifications:
# A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.

# A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

def generate_word_list():
  lines_array = []

  with open('the-three-fates.txt', 'r') as file:
    data = file.read().split()
    
    for line in data:
      words_list = line.split()
      lines_array += words_list
  print len(lines_array)
  return lines_array

def histogram(word_list):
  # returns a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
  print(word_list)
  array_of_word_tuples = []
  for index, word in enumerate(word_list):
    word_occurence = word_list.count(word_list[index])
    word_tuple = (word, word_occurence)
    if word_tuple not in array_of_word_tuples:
      array_of_word_tuples.append(word_tuple)
  return array_of_word_tuples

def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  for unique_word, index in histogram:
    if unique_word == word:
      return index
  return 0

words = generate_word_list()
print(words)
# word_histogram = histogram(words)
# word_types = unique_words(word_histogram)
# print word_histogram
# print 'unique words:', word_types
# print frequency('nothing', word_histogram)