import re

def output_file():
  # open file

  with open('nature.txt', 'r') as file:
    # read individual line
    book_string = file.read()
  
  # Split the Introduction apart from the content of the book.
  book_array = book_string.split('INTRODUCTION.\n\n')

  # This is the content of the book.
  book_string_wo_intro = book_array[1]

  # Split the Licensing content from the content of the book.
  book_array = book_string_wo_intro.split('End of the Project Gutenberg EBook of Nature,')
  
  # Contents of book with whitespace removed (at the end of the content).
  book_content = book_array[0].rstrip()

  p = re.compile('\n([A-Z ]+\.)\n')
  result = p.findall(book_content)
  print result

  with open('test.txt', 'w') as new_file:
    new_file.write(book_content)

output_file()