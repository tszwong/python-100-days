from os import system, name


def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')
    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


name_bid = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid_amount = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid_amount:
            highest_bid_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid_amount}.")


while not bidding_finished:
    user_name = input("What is your name?  ")
    user_amount = int(input("What is your bid?  $"))
    other_bidders = input("Are there any other bidders?  ").lower()

    name_bid[user_name] = user_amount
    if other_bidders == "no":
        bidding_finished = True
        clear()
        highest_bidder(name_bid)
    elif other_bidders == "yes":
        clear()

print(name_bid)
