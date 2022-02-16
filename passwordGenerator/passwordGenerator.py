import random


def passwordGenerator():
    """
    Program asks user for input for a random generated password.
    """

    # all possible items that a password may contain
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # asks for user input in three different categories: letters, numbers, symbols
    print("\nPassword Generator\n\nAnswer the following for your generated password")
    num_letters = int(input("How many letters?  "))
    num_numbers = int(input("How many numbers?  "))
    num_symbols = int(input("How many symbols?  "))

    # empty array that will store the random items generated
    generated_password = []
    total_items = 0

    """
    For loops are used to generate a random item and will run x amount of times
    where x is based on user input in beginning of function.
    
    each item is then appended to the empty array generated_password
    """

    for char in range(1, num_letters + 1):
        # generated_password += random.choice(letters)
        generated_password.append(random.choice(letters))
        total_items += 1

    for num in range(1, num_numbers + 1):
        generated_password.append(random.choice(numbers))
        total_items += 1

    for sym in range(1, num_symbols + 1):
        generated_password.append(random.choice(symbols))
        total_items += 1

    """
    The results are displayed back to user and the final generated password
    will be displayed as well.
    
    The random function shuffle.() is used to change the the order the items
    in the array so that a password can have maximized randomization.
    """

    print(f"\nBase on your input, the password will contain the following:\n{generated_password}")

    final_password = ""
    random.shuffle(generated_password)
    print(f"\nShuffled order to create your random password:\n{generated_password}")

    for item in generated_password:
        final_password += item

    print(f"\nYour password contains {total_items} items.\nYour generated password: {final_password}")


passwordGenerator()
