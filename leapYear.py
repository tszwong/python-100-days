# checks the condition of a leap year and displays the results
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 != 0:
            return False
    else:
        return False


def daysInMonth(year, month):
    num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_per_month = {
        "January": num_days[0],
        "February": num_days[1],
        "March": num_days[2],
        "April": num_days[3],
        "May": num_days[4],
        "June": num_days[5],
        "July": num_days[6],
        "August": num_days[7],
        "September": num_days[8],
        "October": num_days[9],
        "November": num_days[10],
        "December": num_days[11],
    }
    if isLeapYear(year):
        if month == "February":
            return days_per_month["February"] + 1
        else:
            return days_per_month[month]
    else:
        return days_per_month[month]


user_year = int(input("Enter a year:  "))
user_month = input("Enter a month:  ").title()

isLeapYear(year=user_year)
print(f"There are {daysInMonth(year=user_year, month=user_month)} days in {user_month}/{user_year}.")
