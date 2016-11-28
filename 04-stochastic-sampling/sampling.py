# Sampling.py: Function that takes a histogram (however you've structured yours) and returns a single word, at random. It should not yet take into account the distributions of the words.

import random

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
  return sorted(word_list)


def histogram(word_list):
  # Returns a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
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
  return word_tuples_list


def tokens(list_of_tuples):
  tokens = 0
  for word, count in list_of_tuples:
    tokens += count
  return tokens


def probability(list_of_tuples, tokens):
  # Types: total unique words
  # Tokens: total concrete particulars
  word_list_probability = []

  for word, count in list_of_tuples:
    word_probability = (float(count) / tokens)
    word_list_probability.append((word, word_probability))
  return word_list_probability


def ranges(word_probability_list):
  word_range_list = []
  max_value = 0
  for word, probability in word_probability_list:
    max_value += probability
    word_range_list.append((word, max_value))
  return word_range_list


def random_float(word_probability_list):
  return random.random()


def select_random_word(word_range_list, random_number):
  for word, range in word_range_list:
    if random_number <= range:
      return word 



if __name__ == '__main__':
  words = generate_word_list()
  print 'original_word_list:', words

  sorted_word_list = sort_word_list(words)
  print 'sorted_word_list:', sorted_word_list

  words_histogram = histogram(sorted_word_list)
  print 'words_histogram:', words_histogram

  word_tokens = tokens(words_histogram)
  print 'word_tokens:', word_tokens

  word_probability_list = probability(words_histogram, word_tokens)
  print 'word_probability_list:', word_probability_list

  word_range_list = ranges(word_probability_list)
  print 'word_range_list:', word_range_list

  random_number = random_float(word_probability_list)
  print 'random_number:', random_number

  randomly_generated_word = select_random_word(word_range_list, random_number)
  print 'randomly_generated_word:', randomly_generated_word