# Prints a random Monty Python quote. Will only be run as a script because all lines are always executed.
import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

# pick a random number between 0 and 2 (the index of the string in the tuple)
rand_index = random.randint(0, len(quotes) - 1)

# output the random string
print quotes[rand_index]