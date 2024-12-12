import sys
from valid_word import is_valid_word

if len(sys.argv) > 4:
  print(is_valid_word(sys.argv[1], sys.argv[2].split(','), sys.argv[3],sys.argv[4].split(",")))
else:
  print('Be sure to pass in four (4) inputs to the function, first is the word,  second is the letters, third is the required letter, and fourth is the used words. Ex: ' + sys.argv[0] + 'MEAT M,A,C,T,H,E,I H CHAT,THAT')