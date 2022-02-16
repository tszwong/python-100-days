import random
from os import system, name


def clear():
    """
    clears the console
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# the hands of the user and dealer before any card is dealt
user_cards = []
dealer_cards = []


def deal_card(hand):
    """
    adds a random card to the hand(user_cards and/or dealer_cards) that is chosen
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))


def blackjack():
    """
    - Starts the game of blackjack
    - Checks and compares scores of the user's hand and dealer's hand
    - print outcome of results
    """

    # begins the game by assigning two cards to both user and dealer
    for card in range(2):
        deal_card(user_cards)
        deal_card(dealer_cards)

    # shows the cards of user and one of dealer's cards as well the user's card score
    user_cards_sum = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_cards_sum}\nDealer's card: {dealer_cards[0]}")

    if user_cards_sum == 21:
        print("YOU WIN. GAME OVER.")

    # The rules of Blackjack allow the user to choose whether the ace counts as 1 or 11 if the sum of the card do not
    # equal 21(soft). If over 21(hard), which is impossible to occur in just 2 cards --> ace will count as 1
    if 11 in user_cards:
        change_ace_value = input("You have been dealt an Ace. Do you wish to change the value of your ace to 1 or"
                                 " remain 11. Type '1' or '11':  ")
        if change_ace_value == "1":
            for ace, card in enumerate(user_cards):
                if card == 11:
                    user_cards[ace] = 1
                    new_card_sum = sum(user_cards)
                    print(f"Your new cards: {user_cards}, current score: {new_card_sum}")

    # checks the scoring conditions of the game and allow user to make choose of hit(add card) or stand(no card added)
    end_condition = user_cards_sum
    while end_condition < 21:
        game_continue = input("\nHit or Stand? Type 'h' or 's':  ").lower()

        # hit will add a card to user hand, calculate sum of the cards and print out a result
        # if the conditions to end game are met
        if game_continue == "h":
            deal_card(user_cards)
            user_cards_sum = sum(user_cards)
            print(f"Your Cards: {user_cards}, Score: {user_cards_sum}")
            if user_cards_sum > 21:
                print(f"\nBUST, Your Score: {user_cards_sum}")
                end_condition = user_cards_sum
            elif user_cards_sum == 21:
                print("\nBLACKJACK, YOU WIN. GAME OVER.")
                return

        # stand will move on from user to dealer by revealing what cards the dealer has and will print out results
        # based on the sum of the hand. As stated in the rules, if sum of dealer cards are under 14 the deal must
        # take another card. Final results are then printed out.
        elif game_continue == "s":
            print(f"Dealer's Cards: {dealer_cards}\n")
            if sum(dealer_cards) < 14:
                deal_card(dealer_cards)
                print(f"Dealer's Cards: {dealer_cards}, Dealer Card Score: {sum(dealer_cards)}\n")
                if sum(dealer_cards) < sum(user_cards):
                    print("USER WINS.")
                elif sum(dealer_cards) > sum(user_cards):
                    print("YOU LOSE. DEALER WINS.")
                elif sum(dealer_cards) == sum(user_cards):
                    print("TIE.")
            elif sum(dealer_cards) == 21:
                print("DEALER WINS WITH BLACKJACK")
            else:
                clear()
                print(f"Dealer Card Score: {sum(dealer_cards)}\nYour Card Score: {sum(user_cards)}\n")
                if sum(dealer_cards) < user_cards_sum:
                    print("USER WINS.")
                elif sum(dealer_cards) > user_cards_sum:
                    print("YOU LOSE. DEALER WINS.")
                elif sum(dealer_cards) == sum(user_cards):
                    print("TIE.")
            end_condition = 22
        else:
            print("Invalid Response.")

    # checks to see if end condition is met. If met, user will be prompted question to
    # ask if they wish to play another game of blackjack
    if end_condition == 22:
        game()


def game_start():
    """
    initializes game blackjack() or ends the program
    """
    start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()
    if start == "y":
        clear()
        blackjack()
    else:
        clear()
        return


game()
