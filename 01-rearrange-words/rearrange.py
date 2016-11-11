# Rearrange.py: Randomly rearranges a set of words provided as command-line arguments to the script.

# module needed to work with command-line arguments.
import sys

# module needed to use random number generators.
import random

# variable to store new shuffled list.
new_word_list = []

# variable to store randomly selected indices.
indices = []

# pick a random number between 1 and last element of the arguments (excludes first argument, filename).
def randomly_generated_sys_word():
  rand_index = random.randint(1, len(sys.argv) - 1)
  if rand_index in indices:
    rand_index = random.randint(1, len(sys.argv) - 1)
  else:
    indices.append(rand_index)
    print indices
    # output random index of system command-line arguments between 1 and last element.
    return sys.argv[rand_index]

if __name__ == '__main__':
  random_sys_word = randomly_generated_sys_word()
  new_word_list = random_sys_word
  print new_word_list