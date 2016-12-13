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
  book_string_wo_intro = book_array[1]

  # Split the Licensing content from the content of the book.
  book_array = book_string_wo_intro.split('End of the Project Gutenberg EBook of Nature,')
  
  # Contents of book
  book_content = book_array[0]

  # Remove whitespace at the end of the content.
  print book_content.rstrip()


output_file()