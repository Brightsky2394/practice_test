#!/usr/bin/python3

# is_leap_year: check whether an inputted year is leap or not

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

test_list = []
test_result = [False, True, True, False]
number = int(input("Enter the number of list items: "))
if number > 4:
    print("Test cannot be achieved")
else:
    for i in range(number):
        value = int(input("Enter the item value: "))
        test_list.append(value)
print(test_list)
for j in range(len(test_list)):
    yr = test_list[j]
    print(yr, '->', end='')
    result = is_leap_year(yr)
    if result == test_result[j]:
        print("Ok")
    else:
        print("Failed")
