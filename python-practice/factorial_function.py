#!/usr/bin/python3

# factorial_fun: determine the factorial of positive integer
#return - the factorial value of the specified number

def factorial_fun(num):
    if num < 0:
        return None
    elif num < 2:
        return 1
    
    total = 1

    for k in range(2, num + 1):
        total *= k
    return total

num = int(input("Enter any positive integer of your choice: "))

print(num,'!', '=', factorial_fun(num))



