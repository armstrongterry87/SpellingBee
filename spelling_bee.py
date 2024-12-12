# DO NOT REMOVE
from get_word import get_word                 #
from score import get_point_value               # 
from valid_word import is_valid_word            #
#################################################

def spelling_bee():
  
    letters_input = input("Welcome to Spelling Bee! Enter your 7 letters, separated by commas:\n")
    letters = letters_input.replace(" ", "").split(",")  # Convert input to a list, removing spaces if any
    
    # Validate the required letter
    while True:
        required_letter = input(f"Which of these 7 letters {letters} will be your required letter?\n")
        if required_letter in letters:
            break  # Exit the loop if the required letter is valid
        else:
            print(f"{required_letter} is not an available letter. Please choose from the following: {letters}")
    
    # Initialize used words list and score
    used_words = []
    score = 0
    
    # Main game loop
    while True:
        # Prompt for word input
        word = input("Enter your word:\n")
        
        # End the game if the user enters "END"
        if word == "END":
            print(f"Your final score is {score}")
            break
        
        # Check if the word is valid
        if is_valid_word(word, letters, required_letter, used_words):
            # Add valid word to used words and calculate points
            used_words.append(word)
            points = get_point_value(word, letters)
            score += points
        else:
            # If the word is invalid, display the error message without repeating the prompt
            continue

spelling_bee()