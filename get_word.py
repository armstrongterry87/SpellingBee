from valid_word import is_valid_word # DO NOT MODIFY

# Write the get_word function here.
def get_word(letters, required_letter, used_words):
  while True:

    word = input("Enter your word:\n")

    if is_valid_word(word, letters, required_letter, used_words):
      return word