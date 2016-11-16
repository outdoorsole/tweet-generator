# Sampling.py: Function that takes a histogram (however you've structured yours) and returns a single word, at random. It should not yet take into account the distributions of the words.

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
  word_types = 0
  word_tokens = 0
  array_of_word_tuples = []
  for index, word in enumerate(word_list):
    word_occurence = word_list.count(word_list[index])
    word_tuple = (word, word_occurence)
    if word_tuple not in array_of_word_tuples:
      array_of_word_tuples.append(word_tuple)
  for word, token in array_of_word_tuples:
    print token
    word_tokens += token
    print "this: ", word_tokens
  return array_of_word_tuples, word_types, word_tokens

def probability(list_of_tuples, word_tokens):
  word_list_probability = []
  for word, token in list_of_tuples:
    print word, token, word_tokens
    word_probability = (float(token) / word_tokens)
    print "word_probability ", word_probability
    word_list_probability.append((word, word_probability))
  return word_list_probability

def random_word(word_list):
  print 'random'

if __name__ == '__main__':
  words = generate_word_list()
  word_histogram, total_words, unique_words = histogram(words)
  print word_histogram, total_words, unique_words
  word_probability_array = probability(word_histogram, unique_words)
  print word_probability_array