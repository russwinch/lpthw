#!/usr/local/bin/python3
'''
LPTHW exercise 44b
Override Explicitly
'''

class Parent():

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
