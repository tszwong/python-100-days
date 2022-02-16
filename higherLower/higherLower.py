import random
from os import system, name
from higherLowerData import data


def clear():
    """
    clears the console
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def game_start():
    """
    initialization of game
    """
    begin = input("Do you want to play Higher Lower? Type 'y' or 'n':  ").lower()
    if begin == "y":
        clear()
        game()
    else:
        clear()
        return


user_game_score = 0
new_list = []
name_list = []
num_list = []


def restart_game():
    """
    clears the items in the three lists(new_list, name_list, num_list) after each round when user wins
    """
    remove_items = True

    while remove_items:
        if len(new_list) != 0:
            del new_list[0]
            del name_list[0]
            del num_list[0]
        else:
            remove_items = False


def game():
    """
    logic of the game
    """
    global user_game_score
    game_continue = True

    while game_continue:
        for i in range(2):
            new_list.append(random.choice(data))
        # print(new_list)
        for item in new_list:
            name_list.append(item["name"])
            num_list.append(int(item["follower_count"]))

        # game is restarted if the item appended from data to new_list is identical
        if new_list[0] == new_list[1]:
            restart_game()
            game()

        print(f"Your Current Score: {user_game_score}")
        print(f"\nWho has more items?\nCompare A: {name_list[0]}\nAgainst B: {name_list[1]}")
        compare_question = input("Who has more followers? Type 'A' or 'B':  ").upper()
        print()

        # checks if the user input matches the correct answer
        # game will restart and cleared to be ran again
        if num_list[0] < num_list[1]:
            if compare_question == "B":
                user_game_score += 1
                restart_game()
                clear()
            elif compare_question == "A":
                clear()
                print(f"Your Final Score: {user_game_score}")
                user_game_score = 0
                game_continue = False

                # gives user the option to run the program again
                play_again = input("Return to start? Type 'y' or 'n':  ").lower()
                if play_again == "y":
                    clear()
                    game_start()
                elif play_again == "n":
                    return

        elif num_list[0] > num_list[1]:
            if compare_question == "A":
                user_game_score += 1
                restart_game()
                clear()
            elif compare_question == "B":
                clear()
                print(f"Your Final Score: {user_game_score}")
                user_game_score = 0
                game_continue = False
                play_again = input("Return to start? Type 'y' or 'n':  ").lower()
                if play_again == "y":
                    clear()
                    game_start()
                elif play_again == "n":
                    return


game_start()
