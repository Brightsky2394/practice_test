#!/usr/bin/python3
"""
Module that determine number
of weekdays in a given year
"""


import calendar


class MyCalendar(calendar.Calendar):
    """
    MyCalendar class inherits from
    the calendar.Calendar class
    """

    
    def count_weekday_in_year(self, year, weekday):
        """
        method that determine the weekday
        count in a year.
        """
        current_month = 1
        number_of_days = 0
        while current_month <= 12:
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days += 1
            current_month += 1
        return number_of_days

my_calendar = MyCalendar()
year = int(input("Enter the year you want to: "))
weekday_constant = int(input("Enter any number in the range 0-6 (MONDAY - SUNDAY):"))
number_of_days = my_calendar.count_weekday_in_year(year,weekday_constant)
print(number_of_days)
