# program greeting
print("Hello, welcome to Two-Digit Add")

# ask user for input
user_two_digit = input("Please enter a two digit number:  ")

# convert user input from string to int
# the converted user input is then added together
add_values = int(user_two_digit[0]) + int(user_two_digit[1])

# results are displayed in a message after add_values is converted to a string
print("Result:  " + str(add_values))