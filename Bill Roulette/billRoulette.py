import random

# program introduction
print("Roulette\nThe individual chosen will die.\n")

# ask for user input, splicing the user input with ", "
names_list = input("Enter the names of all the individuals in the following format - x, y, z  :  ")
names = names_list.split(", ")

# finding the length of the user input to put into an array later
len_names = len(names)
str_len_names = str(len_names)
print(f"There are {str_len_names} people participating.")

# or random_name = random.choice(names)
# random number is generated with the range dependent on the number of individuals the user inputed
# the corresponding array indices will then be printed
random_name = random.randint(0, len_names - 1)
chosen = f"{(names[random_name])} will die."

# confirmation to continue and display of results
confirm = input("\nWe have the results. Confirm to continue (Yes or No):  ")
if confirm == "Yes":
    print(chosen)
elif confirm == "No":
    print("End")
else:
    print("Error: Invalid response, please enter Yes or No")
