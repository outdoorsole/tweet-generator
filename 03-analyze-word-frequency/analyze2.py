# Analyze.py
# Performs Text Analysis on the frequency of words within a body of source text.

# Specifications:
# A histogram() function which takes a source_text argument (can be either a filename or the contents of the file as a string, your choice) and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.

# A unique_words() function that takes a histogram argument and returns the total count of unique words in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.

# A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text. For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.

def generate_word_list():
  # Create file object using the open() function to process the text file.
  # Specify the context using the with statement. A file object is a context manager; the with statement uses the file as a manager. OS resources are released when Python files are closed.
  with open('words.txt') as file:
    # Read entire file into a single string.
    text = file.read()
    # Return a list of words from the string.
    words_list = text.split()
  return words_list

def sort_word_list(word_list):
  # return sorted(word_list, key = lambda x: x[0])
  return sorted(word_list)

def histogram(word_list):
  print(word_list)
  array_of_word_tuples = []
  for index, word in enumerate(word_list):
    word_occurence = word_list.count(word_list[index])
    word_tuple = (word, word_occurence)
    if word_tuple not in array_of_word_tuples:
      array_of_word_tuples.append(word_tuple)
  return array_of_word_tuples

def unique_words(histogram):
  return None

def frequency(word, histogram):
  return None

if __name__ == '__main__':
  words = generate_word_list()
  print words
  # words_histogram = histogram(words)
  print sort_word_list(words)