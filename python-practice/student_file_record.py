#!/usr/bin/python3

"""
Open student file record,
perform the total of the
score, and sort the name
in alphabetical order
"""


class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

dict_record = dict()
file_name = input("Enter student file name: ")

try:
    fd = open(file_name, 'rt')
    lines = fd.readlines()
    fd.close()

    if len(lines) == 0:
        raise FileEmpty()
    for j in range(len(lines)):
        line = lines[j]
        columns = line.split()
        if len(columns) > 3:
            raise WrongLine(j + 1, line)
        student = columns[0] + ' ' + columns[1]
        try:
            val_points = float(columns[2])
        except ValueError:
            raise WrongLine(j + 1, line)

        try:
            dict_record[student] += val_points
        except KeyError:
            dict_record[student] = val_points

    for student in sorted(dict_record.keys()):
        print(student, '\t', dict_record[student])

except IOError as e:
    print("I/O error occurred", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_string) + " in source file" + e.line_string)
except FileEmpty:
    print("Source file is empty")

