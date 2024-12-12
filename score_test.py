import sys
from score import get_point_value

if len(sys.argv) > 2:
  print(get_point_value(sys.argv[1],sys.argv[2].split(',')))
else:
  print('Remember to include the letters, required letter, and used guesses, e.g: ' + sys.argv[0] + '  MATCHTIME M,A,C,T,H,E,I')