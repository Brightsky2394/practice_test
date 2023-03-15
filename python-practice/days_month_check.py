#!/usr/bin/python3

# is_leap_year: check whether an inputted year is leap or not
# return: True otherwise False

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# days_in_month: validate whether a given days of a particular month is correct or not
# return: Ok if True and otherwise Failed

def days_in_month(year, month):
    if year < 1582 or month < 0 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_leap_year(year):
        res = 29
    return res

test_year = []
test_month = []
num = int(input("Enter the number of list items: "))
if num > 4 or num <= 0:
    print("Can't validate test")
else:
    for i in range(num):
        val1 = int(input("Enter the test_year item(four digit for year): "))
        val2 = int(input("Enter the test_month items(choose any number from 1 to 12): "))
        test_year.append(val1)
        test_month.append(val2)
print(test_year)
print(test_month)

test_result = [28, 29, 31, 30]
for j in range(len(test_year)):
    yr = test_year[j]
    mon = test_month[j]
    print(yr, mon, '->', end='')
    result = days_in_month(yr, mon)
    if result == test_result[j]:
        print("Ok")
    else:
        print("Failed")
    
