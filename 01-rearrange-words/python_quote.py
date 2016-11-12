# Prints a random Monty Python quote (will be run as an independent module). This file is also dual purpose, serving as both an executable and a module. This uses a conditional to allow the program to run 
import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

# pick a random number between 0 and 2 (the index of the string in the tuple)
def random_python_quote():
  rand_index = random.randint(0, len(quotes) - 1)
  return quotes[rand_index]

if __name__ == '__main__':
  quote = random_python_quote()
  # output the random string
  print quote