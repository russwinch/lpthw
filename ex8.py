#!/usr/local/bin/python3
'''
LPTHW exercise 8
Printing, Printing
'''

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "here",
    "is",
    "some",
    "text"))
