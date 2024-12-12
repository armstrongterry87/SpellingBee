def is_pangram(guess, letters):
  for i in letters:
    if i not in guess:
      return False
  return True