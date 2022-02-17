from os import system, name
from menu import MENU, resources
import sys


def clear():
    """
    clears the console
    """
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


ingredients_required = {}
profit = 0


def coin_insert():
    """
    :return: the total sum of coins inserted by the user
    """
    num_quarters = int(input("Number of quarters:  ")) * 0.25
    num_dimes = int(input("Number of dimes:  ")) * 0.10
    num_nickels = int(input("Number of nickels:  ")) * 0.05
    num_pennies = int(input("Number of pennies:  ")) * 0.01

    total = num_quarters + num_dimes + num_nickels + num_pennies

    return total


def drink_selection(drink):
    """
    :param drink: adds the ingredients of selected drink into ingredients_required and the cost of the drink into drink_costs
    :return drink_costs:
    """
    global ingredients_required
    drink_costs = []

    if drink == "espresso":
        drink_costs.append(MENU["espresso"]["cost"])
        ingredients_required = MENU["espresso"]["ingredients"]
    elif drink == "latte":
        drink_costs.append(MENU["latte"]["cost"])
        ingredients_required = MENU["latte"]["ingredients"]
    elif drink == "cappuccino":
        drink_costs.append(MENU["cappuccino"]["cost"])
        ingredients_required = MENU["cappuccino"]["ingredients"]

    return drink_costs


def enough_resources():
    """
    checks if the machine has enough resource in it to make the selected drink
    :return True/False: based on conditions checked
    """
    for item in ingredients_required:
        if ingredients_required[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def transaction_status(drink_cost):
    """
    :param drink_cost: cost of the drink selected by user
    :return True/False: status based on amount paid by user and cost of drink
    """
    global profit
    amount_paid = coin_insert()
    cost_of_drink = drink_cost[0]

    # checks how the amount paid by user compares to the cost of drink selected
    if amount_paid < cost_of_drink:
        return False
    elif amount_paid == cost_of_drink:
        profit += cost_of_drink
        return True
    elif amount_paid > cost_of_drink:
        clear()
        change_given = amount_paid - cost_of_drink
        print(f"Your change: ${round(change_given, 2)}")
        profit += cost_of_drink
        return True
    else:
        return False


def resources_deduct():
    """
    :return: update resources after ingredients are deducted from resource total
    """
    global resources
    for item in ingredients_required:
        # subtracts the required ingredients used for a drink from resources
        resources[item] -= ingredients_required[item]

    return resources, ingredients_required


def add_resources():
    """
    refills the resources in the machine by setting the values of each value back to default and
    subtracts 1.00 from profit for cost of refill
    """
    global resources
    global profit

    profit -= 1.00

    # replaces the values of resources to the new set values
    for item in resources:
        if item == "water":
            resources[item] = 500
        elif item == "milk":
            resources[item] = 450
        elif item == "coffee":
            resources[item] = 400


machine_on = True

while machine_on:
    drink_select = input("What would you like to drink? (espresso/latte/cappuccino):  ")
    clear()
    if drink_select == "off":
        machine_on = False
        sys.exit() # terminates the program
    elif drink_select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif drink_select == "refill":
        add_resources()
    elif drink_select == "profit":
        print(f"Current Profit: ${profit}")
    else:
        if drink_select in MENU:
            if transaction_status(drink_cost=drink_selection(drink=drink_select)):
                if enough_resources():
                    print(f"Transaction Successful. Enjoy your {drink_select}.\n")
                    resources_deduct()
                else:
                    print("Sorry, not enough resources for your drink.")
            else:
                clear()
                print("Not Enough Money. Refunded.")
