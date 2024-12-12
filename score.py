from pangram import is_pangram #DO NOT MODIFY
def get_point_value(word,letters):
  points = len(word)
    
    # Check if the word is a pangram
  if is_pangram(word, letters):
    points += 7
    print(f"{word} - Pangram!")
  else:
    print(word)
    
  return points