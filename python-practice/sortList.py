#!/usr/bin/python3
# The code before the first print add element to
# an empty list through user interaction.
my_list = []
number = int(input("Enter the number of list items: "))
for i in range(number):
    value = float(input("Enter the list item value: "))
    my_list.append(value)
print(my_list)

# The code is now sorted in ascending order i.e
# from the smallest number to the biggest.

swapped = True
while swapped:
    swapped = False
    for j in range(len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:
            swapped = True
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
print("\nSorted")
print(my_list)
