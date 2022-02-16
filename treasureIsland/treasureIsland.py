# program introduction
print("\nWelcome to Treasure Island. Your mission is to find the treasure.\n")
print('''
                               ____
                  _           |---||            _
                  ||__________|SSt||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,

            ''')

# initial user choice
choice1_left_right = input("You have approached a cross road! Will you go to left or right? (Enter left or right): ")

# results
end = "**** GAME OVER ****"
win = "**** YOU HAVE WON! YOU FOUND THE TREASURE ****"

# scenarios based on user inputs
if choice1_left_right == "left":
    swim_wait = input("There is a house in sight! You can go take the trail or the shortcut which "
                      "is to swim through the pond. Will you take the trail or swim? (Enter trail or swim):  ")
    if swim_wait == "trail":
        door_selection = input("There are three doors here! Pick one of the following: red, blue, yellow  ")
        if door_selection == "red":
            print("You have been burned by fire!")
            print("\n" + end)
        elif door_selection == "yellow":
            print("\n" + win)
        elif door_selection == "blue":
            print("You have been eaten by a lion!")
            print("\n" + end)
        else:
            print(end + ": Please enter one of the three valid options")
    else:
        print("You have been eaten by a crocodile!")
        print("\n" + end)
else:
    print("Oh no! You have fallen into a hole!")
    print(end)
