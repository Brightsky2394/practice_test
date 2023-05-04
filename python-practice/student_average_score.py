#!/usr/bin/python3

# evaluate the average score of students
# uses both dictionary and tuple for storing data
# return - the expected average

school_class = {}
while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    score = int(input("Enter the student score (0 - 10): "))
    if score not in range(0, 11):
        break
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
for name in school_class.keys():
    the_add = 0
    count = 0
    for Score in school_class[name]:
        the_add += Score
        count += 1
    print(name, "average score is: ", the_add / count)
