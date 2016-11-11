# Rearrange.py: Randomly rearranges a set of words provided as command-line arguments to the script.

# module needed to work with command-line arguments.
import sys

# module needed to use random number generators.
import random

# pick a random number between 1 and last element of the arguments (excludes first argument, filename).
def randomly_generated_sys_word():
  rand_index = random.randint(1, len(sys.argv) - 1)
  # output random index of system command-line arguments between 1 and last element.
  return sys.argv[rand_index]

if __name__ == '__main__':
  random_sys_word = randomly_generated_sys_word()
  # output the randomly generated index.
  print random_sys_word
