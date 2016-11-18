# Sampling.py: Function that takes a histogram (however you've structured yours) and returns a single word, at random. It should not yet take into account the distributions of the words.

def generate_word_list():
  # Create file object using the open() function to process the text file.
  # Specify the context using the with statement. A file object is a context manager; the with statement uses the file as a manager. OS resources are released when Python files are closed.
  with open('the-three-fates.txt') as file:
    # Read entire file into a single string.
    text = file.read()
    # Return a list of words from the string.
    words_list = text.split()
  return words_list

def histogram(word_list):
  # returns a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
  word_tuples_list = []
  count = 1
  counter = 0

  if len(word_list) <= 1:
    return [(word_tuple, count) for word_tuple in word_list]

  for index in range(len(word_list) - 1):
    if word_list[index] == word_list[index + 1]:
      count += 1
    else:
      word_tuple = (word_list[index], count)
      word_tuples_list.append(word_tuple)
      count = 1
    counter += 1
  if count > 1 or word_list[-1] != word_list[-2]:
    word_tuple = (word_list[-1], count)
    word_tuples_list.append(word_tuple)
  print count
  print counter
  return word_tuples_list


def probability(list_of_tuples, word_tokens):
  word_list_probability = []
  for word, token in list_of_tuples:
    print word, token, word_tokens
    word_probability = (float(token) / word_tokens)
    word_list_probability.append((word, word_probability))
  return word_list_probability

def random_word(word_list):
  print 'random'

if __name__ == '__main__':
  words = generate_word_list()
  print words
  # word_histogram, total_words, unique_words = histogram(words)
  # print word_histogram, total_words, unique_words
  # word_probability_array = probability(word_histogram, unique_words)
  # print word_probability_array