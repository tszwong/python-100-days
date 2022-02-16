# program greetings
print("Pizza Delivery Order")

# displaying menu for user
menu_display = "Menu:\nSmall Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25" \
               "\n\nPepperoni for Small Pizza: +$2\nPepperoni for Medium/Large Pizza: +$3\n" \
               "Extra cheese for pizza of any size: +$1"
print(menu_display)

# assigning prices to variables and asking user for input
pizza_small_price = 15
pizza_medium_price = 20
pizza_large_price = 25

pizza_size = input("\nWhat size pizza do you want to order? S, M, or L  ")
pepperoni_add = input("Do you want to add pepperoni?  Y or N  ")
cheese_extra = input("Do you want extra cheese?  Y or N  ")

# bill message
final_bill_message = "Your total is: $"

# checks the user inputs and display message with final bill based on the inputs
if pizza_size == "S":
    if pepperoni_add == "Y":
        pizza_small_price += 2
        if cheese_extra == "Y":
            pizza_small_price += 1
            print(final_bill_message + str(pizza_small_price))
        elif cheese_extra == "N":
            print(final_bill_message + str(pizza_small_price))
        else:
            print("Error: Please Enter Y or N")
    elif pepperoni_add == "N":
        print(final_bill_message + str(pizza_small_price))
    else:
        print("Error: Please Enter Y or N")
elif pizza_size == "M":
    if pepperoni_add == "Y":
        pizza_medium_price += 3
        if cheese_extra == "Y":
            pizza_medium_price += 1
            print(final_bill_message + str(pizza_medium_price))
        elif cheese_extra == "N":
            print(final_bill_message + str(pizza_medium_price))
        else:
            print("Error: Please Enter Y or N")
    elif pepperoni_add == "N":
        print(final_bill_message + str(pizza_medium_price))
    else:
        print("Error: Please Enter Y or N")
elif pizza_size == "L":
    if pepperoni_add == "Y":
        pizza_large_price += 3
        if cheese_extra == "Y":
            pizza_large_price += 1
            print(final_bill_message + str(pizza_large_price))
        elif cheese_extra == "N":
            print(final_bill_message + str(pizza_large_price))
        else:
            print("Error: Please Enter Y or N")
    elif pepperoni_add == "N":
        print(final_bill_message + str(pizza_large_price))
    else:
        print("Error: Please Enter Y or N")
else:
    print("Error: Please enter one of the three valid pizza sizes.")
