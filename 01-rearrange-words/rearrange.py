# Rearrange.py: Randomly rearranges a set of words provided as command-line arguments to the script.

# module needed to work with command-line arguments.
import sys

# module needed to use random number generators.
import random

# create a new list, which excludes first argument, filename.
def sys_word_list():
  # variable to store new shuffled list.
  word_list = []
  
  for word in sys.argv:
    word_list.append(word)

  # remove the first element (filename).
  word_list.pop(0)
  return word_list

# pick a random number between 1 and last element of the arguments (excludes first argument, filename).
def random_index_generator(word_list):
  rand_index = random.randint(1, len(word_list) - 1)
  return rand_index

def shuffle_words(word_list):
  for inital_index, word in enumerate(word_list):

    # variable to store randomly selected indices.
    new_index = random_index_generator(word_list)

    # swap two words by index.
    word_list[inital_index], word_list[new_index] = word_list[new_index], word_list[inital_index]

  return word_list


if __name__ == '__main__':
  sys_arg_word_list = sys_word_list()
  print 'sys_arg_word_list:', sys_arg_word_list

  shuffled_list = shuffle_words(sys_arg_word_list)
  print 'shuffled_list:', shuffled_list