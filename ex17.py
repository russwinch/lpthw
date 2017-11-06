#!/usr/local/bin/python3
'''
LPTHW exercise 17
More Files
'''

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

# in_file = open(from_file)
# indata = in_file.read()
# in_file.close()
indata = open(from_file).read() # more efficient than the above

if exists(to_file):
    input("file already exists. hit RETURN to overwrite or ^C to cancel: ")
out_file = open(to_file, 'w')
out_file.truncate() # only matters for existing files
out_file.write(indata)
out_file.close()

print("copy complete")
