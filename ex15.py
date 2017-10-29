#!/usr/local/bin/python3
'''
LPTHW exercise 15
Reading Files
'''

from sys import argv
script, filename = argv

txt = open(filename)

print(f"heres your file {filename}")
print(txt.read())
txt.close()

file_again = input("type the filename again:")
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
