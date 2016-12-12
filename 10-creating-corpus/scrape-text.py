import re

def output_file():
  # open file
  file = open('nature.txt')
  # read individual line
  book_string = file.read()
  file.close()
  
  word_list = re.split('(\W+)', book_string)
  
  new_file = open('test.txt', 'a')
  for word in word_list:
    print word
    new_file.write(word)

  # print word_list


  # new_sentence_list = []
  # for sentence in sentence_list:
  #   new_sentence = sentence.strip('\n')
  #   print new_sentence
  #   new_sentence_list.append(new_sentence)
  # print new_sentence_list

output_file()