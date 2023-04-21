#!/usr/bin/python3

# is_triangle: to formulate whether triangle can be formed from the given length
# return - Boolean value True or False

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

# heron: calculate the area of the given triangle
# return - the area desired value

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# area: validate the triangle
# return: the area of the triangle

def area(a, b, c):
    if not is_triangle(a, b, c):
        return None
    else:
        return heron(a, b, c)

a = float(input("Enter the first side's of the length: "))
b = float(input("Enter the second side's of the length: "))
c = float(input("Enter the third side's of the length: "))

print(is_triangle(a, b, c))
print(area(a, b, c))

