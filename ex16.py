#!/usr/local/bin/python3
'''
LPTHW exercise 16
Reading and Writing Files
'''
from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit ^C.")
print("To confirm and erase press RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file...")
target.truncate()

print("Now enter 3 lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Writing new lines to the file...")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally close the file...")
target.close()
