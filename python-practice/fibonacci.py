#!/usr/bin/python3

def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

r = int(input("Enter the list of number to print: "))
for n in range(1, r):
    print(fib(n), end=' ')


