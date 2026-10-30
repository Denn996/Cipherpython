#Leap year checker

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False

try:
    year_input = int(input("Enter a year: "))

    if is_leap_year(year_input):
        print(f"{year_input} is a leap year (366 days).")

    else:
        print(f"{year_input} is not a leap year (365 days).")


except ValueError:
    print("Invalid input! Please enter a vlaid integer year.")