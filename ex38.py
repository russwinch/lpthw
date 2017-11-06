#!/usr/local/bin/python3
'''
LPTHW exercise 38
Doing Things to Lists
'''

ten_things = "apples oranges crows telephone light sugar"

stuff = ten_things.split(' ')
more_stuff = ['day', 'corn', 'night', 'song', 'frisbee', 'banana', 'girl',
        'boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print("there are {} items now".format(len(stuff)))

print("there we go: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
