# program greeting
print("Tip Calculator")

# ask user to input value of bill for tip to be calculated
bill = float(input("What the the total bill of the meal?  $"))

# ask user to select which set percentage of tip they wish to pay
tip_percentage = 0.10, 0.12, 0.15
tip_percentage_user = int(input(f"What percentage tip would you like to pay? 10, 12, or 15?  "))

# ask user to input how many people are paying the total bill with tip
people_total = int(input("How many people to split the bill with?  "))

display_message = "Each person will pay: $"

# checks the user inputs and plug values into equation to determine the amount each person will pay
if tip_percentage_user == 10:
    bill_total = (bill + tip_percentage[0]*bill)/people_total
    final_amount = "{:.2f}".format(bill_total)
    print(f"{display_message}{final_amount}")
elif tip_percentage_user == 12:
    bill_total = (bill + tip_percentage[0]*bill)/people_total
    final_amount = "{:.2f}".format(bill_total)
    print(f"{display_message}{final_amount}")
elif tip_percentage_user == 15:
    bill_total = (bill + tip_percentage[0]*bill)/people_total
    final_amount = "{:.2f}".format(bill_total)
    print(f"{display_message}{final_amount}")
else:
    print("Error: Please enter one of the three valid values for the tip amount")