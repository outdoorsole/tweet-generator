import re

def output_file():
  # open file
  file = open('nature.txt')
  # read individual line
  book_string = file.read()
  file.close()
  
  # Split the Introduction apart from the content of the book.
  book_array = book_string.split('INTRODUCTION.')

  # This is the content of the book.
  print book_array[1]

output_file()