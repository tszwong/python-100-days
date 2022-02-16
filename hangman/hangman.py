import random

""" The program selects a random word out of a selection of words and
        asks the the user to guess the word letter by letter.
    """

# setting the possible words for the game
print("--Welcome to Hangman--")
word_list = ["basketball", "boston", "university", "cat", "dog", "woman", "food", "pineapple",
             "hair", "bed", "pie", "asteroid", "insomnia", "cookies"]

# a random word is chosen for word_list and assigned to the variable chosen_word
# the length of the chosen word will be used to determine the amount of blanks for display
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

# the blanks will be added to an empty array blank_spaces_lines
blank_spaces_lines = []
for i in range(word_len):
    blank_spaces_lines += "_"

# print(chosen_word)

# chosen_word_split = [str(letter) for letter in chosen_word]
# print(chosen_word_split)

# the contents from array blank_space_lines will be printed and joined together in the form of a string
word_to_str = ''.join([str(a) for a in blank_spaces_lines])
print(f"\nYour word is: {word_to_str}")

# sets the game condition and amount of live which is displayed to user
user_lives = 6
game_over = False
print(f"You have {user_lives} lives.")

# the loop will run as long as user have lives left and letters are missing from word
while not game_over and "_" in blank_spaces_lines:
    user_guess = input("\nGuess a letter:  ").lower()

    # if the guess from the user is correct, the letter will replace the corresponding blanks
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == user_guess:
            print(f"The letter {user_guess} is in the word.")
            blank_spaces_lines[position] = user_guess
            user_lives += 0

    # if the guess from user is incorrect then a life will be taken away and if no lives remain the game will end
    if user_guess not in chosen_word:
        user_lives -= 1
        print(f"You have lost a life. You have {user_lives} lives left.")
        if user_lives == 0:
            game_over = True
            print("You have zero lives left. Game over.")

    blanks_to_str = ''.join([str(a) for a in blank_spaces_lines])
    print(f"Your word is: {blanks_to_str}")

    # end condition, if there are no blanks left, which means all letters were correctly guessed, the user wins and
    # program will end
    if "_" not in blank_spaces_lines:
        print(f"\nYou have won! The word is ({chosen_word}).")
