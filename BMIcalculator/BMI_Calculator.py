# program greetings
print("BMI Calculator\n")

# asks the user to input their weight and height
user_weight = input("Please enter your weight(kg):  ")
user_height = input("Please enter your height(m):  ")

# turns the user inputs into numerical values --> float
user_weight_num = float(user_weight)
user_height_num = float(user_height)

# plug user input values into BMI equation and displaying results
bmi_equation_result = user_weight_num/user_height_num**2
print("\nBody Mass Index: " + str(bmi_equation_result))
# print(f"\nBody Mass Index: {bmi_equation_result}") simplified version using f-string

display_message_bmi_range = "Your BMI range is: "

# places user into the different BMI ranges based on their result from the equation
if bmi_equation_result < 18.5:
    print(display_message_bmi_range + "Underweight")
elif bmi_equation_result == 18.5 or 18.5 < bmi_equation_result < 24.9:
    print(display_message_bmi_range + "Normal/Healthy Weight")
elif bmi_equation_result == 24.9 or 24.9 < bmi_equation_result < 29.9:
    print(display_message_bmi_range + "Overweight")
elif bmi_equation_result == 29.9 or 29.9 < bmi_equation_result < 35.0:
    print(display_message_bmi_range + "Obese")
else:
    print(display_message_bmi_range + "Clinically Obese/Jane Pan")
