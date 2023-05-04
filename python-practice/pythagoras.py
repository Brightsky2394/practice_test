#!/usr/bin/python3

# is_triangle: confirm whether triangle can be formed from a given length
# return: Boolean value True or False
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


# pythagoras: determine whether a given triangle is right angle triangle
#  return: Boolean value True or False

def pythagoras(a, b, c):
    if not is_triangle(a, b, c):
        return None
    else:
        if a > b and a > c:
            return (a ** 2 == b ** 2 + c ** 2)
        elif b > a and b > c:
            return (b ** 2 == a ** 2 + c ** 2)
        else:
            return (c ** 2 == a ** 2 + b ** 2)
a = float(input("Enter the first side's of length: "))
b = float(input("Enter the second sides's of length: "))
c = float(input("Enter the third side's of length: "))

print(is_triangle)
print(pythagoras(a, b, c))
