import sys
from get_word import get_word

if len(sys.argv) > 3:
  print(get_word(sys.argv[1].split(','),sys.argv[2],sys.argv[3].split(',')))
else:
  print('Remember to include the letters, required letter, and used words, e.g: ' + sys.argv[0] + ' M,A,C,T,H,E,I H CHAT,THAT')