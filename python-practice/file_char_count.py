#!/usr/bin/python3

"""
count the number of each
individual character in
a text file
"""


from os import strerror

counters = {chr(j): 0 for j in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of file to be analyze: ")

try:
    stream = open(file_name, mode='rt', encoding='utf-8')
    for line in stream:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    stream.close()

    for char in counters.keys():
        cnt = counters[char]
        print(char, '->', cnt)

except IOError as e:
    print("I/O error occurred", strerror(e.errno))
