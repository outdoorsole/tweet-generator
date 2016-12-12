def output_file():
  # open file
  file = open('nature.txt')
  # read individual line
  sentence_list = file.readlines()
  print sentence_list

  new_sentence_list = []
  for sentence in sentence_list:
    new_sentence = sentence.strip('\n')
    print new_sentence
    new_sentence_list.append(new_sentence)
  print new_sentence_list

output_file()