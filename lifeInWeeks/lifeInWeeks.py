# program greetings
print("Life in Weeks")

# asks user to input their age
user_age = input("What is your current age?  ")
user_age_num = int(user_age)

# converts user age into days, weeks, and months
user_age_num_days = user_age_num*365
user_age_num_weeks = user_age_num*52
user_age_num_months = user_age_num*12

# converts max age of 90 years to days, weeks, and months
max_age_days = 90*365
max_age_weeks = 90*52
max_age_months = 90*12

# differences between the max age and user age reveals how much time the user has left in days/weeks/months
time_left_days = max_age_days - user_age_num_days
time_left_weeks = max_age_weeks - user_age_num_weeks
time_left_months = max_age_months - user_age_num_months

# final result display message
display_message = f"You have {time_left_days} days, {time_left_weeks} weeks, and {time_left_months} months left."
print(display_message)