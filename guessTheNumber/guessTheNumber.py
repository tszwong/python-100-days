import random
from os import system, name


def clear():
    """
    clears the console when the function is called
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("Clear")


def game_start():
    """
    Allows user to select difficulty level which will be returned
    """
    print("Guess my number between 1 and 100")
    game_difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard':   ").lower()
    clear()
    return game_difficulty


user_lives = 0


def num_lives(level):
    """
    The number of user lives is assigned to variable user_lives depending on
    what was returned from the game_start() function
    """
    global user_lives
    if level == 'easy':
        user_lives = 10
    elif level == 'hard':
        user_lives = 5


def num_generated():
    """
    Generates and returns a random number from 0 to 100
    """
    num = random.randint(0, 100)
    return num


def guessTheNumber():
    """
    The function containing the entire logic of the game.
    """
    global user_lives
    num_lives(level=game_start())
    correct_number = num_generated()
    clear()

    game_continue = True
    while game_continue:
        user_guess = int(input("Make a guess:  "))
        if user_guess < correct_number:
            print("TOO LOW")
            user_lives -= 1
            print(f"Lives Remaining: {user_lives}\n")
        elif user_guess > correct_number:
            print("TOO HIGH")
            user_lives -= 1
            print(f"Lives Remaining: {user_lives}\n")
        elif user_guess == correct_number:
            clear()
            print(f"CORRECT, the number was: {correct_number}")
            if input("Play Again? Type 'y' or 'n':  ").lower() == 'y':
                clear()
                num_lives(level=game_start())
            else:
                clear()
                return

        if user_lives == 0:
            game_continue = False


guessTheNumber()
