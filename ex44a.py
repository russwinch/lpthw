#!/usr/local/bin/python3
'''
LPTHW exercise 44a
Implicit Inheritance
'''

class Parent():

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
