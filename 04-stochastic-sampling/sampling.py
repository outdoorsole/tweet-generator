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
  array_of_word_tuples = []
  for index, word in enumerate(word_list):
    word_occurence = word_list.count(word_list[index])
    word_tuple = (word, word_occurence)
    if word_tuple not in array_of_word_tuples:
      array_of_word_tuples.append(word_tuple)
  return array_of_word_tuples

def random_word(word_list):
  print 'random'

if __name__ == '__main__':
  words = generate_word_list()
  word_histogram = histogram(words)
  print word_histogram