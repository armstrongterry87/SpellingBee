import sys
from pangram import is_pangram

if len(sys.argv) > 2:
  print(is_pangram(sys.argv[1],sys.argv[2].split(',')))
else:
  print('Remember to include the letters, required letter, and used guesses, e.g: ' + sys.argv[0] + '  MATCHTIME M,A,C,T,H,E,I')