import re

def output_file():
  # open file
  file = open('nature.txt')
  # read individual line
  book_string = file.read()
  file.close()
  
  word_string = re.sub('(\W+)', " ", book_string, )
  pattern = re.compile('(\w+?!.)', book_string)
  print pattern.group(1)

  # word_list = word_string.split(" ")
  # print word_list


  # new_file = open('test.txt', 'a')
  # new_word_list = []
  # for word in word_list:
  #   new_file.write(word)
  #   new_word_list.append(word)

  # print new_word_list


  # new_sentence_list = []
  # for sentence in sentence_list:
  #   new_sentence = sentence.strip('\n')
  #   print new_sentence
  #   new_sentence_list.append(new_sentence)
  # print new_sentence_list

output_file()