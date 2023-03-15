#!/usr/bin/python3

# is_leap_year: check whether a specified year is leap or not
# return - Boolean value i.e True or False

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# day_in_month: determine the exact day of the month
# return - the numerical value of the day

def days_in_month(year, month):
    if year < 1582 or month < 0 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_leap_year(year):
        res = 29
    return res

# days_in_year: evaluate the exact day of the year
# return: numerical value of day

def days_in_year(year, month, day):
    days = 0
    for k in range(1, month):
        data = days_in_month(year, k)
        days += data
    data = days_in_month(year, month)
    if 1 <= day <= data:
        return days + day
    else:
        return None
year = int(input("Enter year value: "))
month = int(input("Enter month value: "))
day = int(input("Enter day value: "))
result = days_in_year(year, month, day)
print("The corresponding day of the year is", result)
