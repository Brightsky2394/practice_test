#!/usr/bin/python3

# is_prime: Check whether given number is prime or number
# return - the passed number if prime, otherwise it return nothing

def is_prime(number):
    for i in range(2, int(1 + number ** 0.5)):
        if number % i == 0:
            return False
    return True

num = int(input("Enter the number of prime to be printed: "))
for j in range(1, num):
    if is_prime(1 + j):
        print(1 + j, end=' ')
print()

