# alphabet array before shift
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']

# user input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("\nType your message: ").lower()
shift = int(input("\nType the shift number: "))


def cipher_encrypt(plain_text, shift_amount):
    """
    the function will turn user input text into a coded message
    by shifting the entire alphabet and reconstructing the word
    """

    # each letter of the user text will be appended into new array user_text_list
    user_text_list = []
    for letter in plain_text:
        user_text_list.append(letter)

    # shift_start shows what the current letter is being appended into shifted alphabet
    current_shift = int(shift_amount)
    shift_start = alphabet[current_shift]
    new_alphabet = []

    # while there are still unchecked values in the array alphabet,
    # new values will be appended to the array new_alphabet
    total_index = len(alphabet)
    while total_index > 0:

        if current_shift == len(alphabet) - 1:
            current_shift -= len(alphabet)

        # total_index will decrease by 1 every time the loop runs as a new letter gets appended to new_alphabet
        # current_shift will increase by 1 as the program checks next value in array alphabet
        shift_start = alphabet[current_shift]
        current_shift += 1
        total_index -= 1
        new_alphabet.append(shift_start)

    cipher_word = []
    for letter in user_text_list:
        letter_index = alphabet.index(letter)
        new_letter = new_alphabet[letter_index]

        # checks for any spaces in the user text --> plain_text, if exists the blank will be entered into cipher_word
        # spaces do not get encrypted in this function
        if letter != " ":
            cipher_word.append(new_letter)
        elif letter == " ":
            cipher_word.append(" ")

    # the values of the array cipher_word will be joined to emulate the user text format and results will be displayed
    final_result = "".join([str(i) for i in cipher_word])
    print(f"Your encoded message: \n{final_result}")

    """
    condensed version of encoding user's text,
    this method encodes plain_text without creating and using a shifted alphabet array

        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    """


def cipher_decode(decrypt_text, decrypt_shift):
    ciphered_text = ""

    # for every letter in the user text --> decrypt_text, the function will find the corresponding index to see where
    # the current letter is at in the alphabet
    for letter in decrypt_text:
        position = alphabet.index(letter)
        # the new position will be the current letter in the alphabet subtracted by
        # shift to get back to the original version without shift
        new_position = position - decrypt_shift

        # checks for spaces in user text --> decrypt_text
        if letter != " ":
            ciphered_text += alphabet[new_position]
        elif letter == " ":
            ciphered_text += " "

    print(f"\nThe decoded text is: {ciphered_text}")


# checks for which function to be called
if direction == "encode":
    cipher_encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    cipher_decode(decrypt_text=text, decrypt_shift=shift)
else:
    print("ERROR, please enter encode or decode.")
