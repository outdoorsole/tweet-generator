# Random-dict-words: Read from a text file, select a random set of words from the file, and put those words together into a "sentence".

import random
import sys

# Reads a file and generates a word list.
def create_word_list():
  file = open("words")

  # variable to store the dictionary words.
  word_list = []

  for word in file:
    word = word.strip('\n')
    word_list.append(word)

  return(word_list)

def get_word_count(word_list):
  return int(sys.argv[1])

def get_random_number_list(word_list, word_count):
    return random.sample(range(len(word_list)), word_count)

def randomize_word_list(word_list, word_count):
    random_number_list = get_random_number_list(word_list, word_count)

    new_word_list = []

    for i in range(len(random_number_list)):
        random_number = random_number_list[i]
        new_word_list.append(word_list[random_number])

    return new_word_list

def convert_list_to_string(word_list):
    return " ".join(word_list)


if __name__ == '__main__':
  dictionary_list = create_word_list()
  word_count = get_word_count(dictionary_list)
  new_dictionary_list = randomize_word_list(dictionary_list, word_count)
  dictionary_string = convert_list_to_string(new_dictionary_list)
  print dictionary_string