#!/usr/local/bin/python3
"""
LPTHW exercise 44e
Composition
"""

class Other():

    def override(self):
        print("Other override()")

    def implicit(self):
        print("Other implicit")

    def altered(self):
        print("Other altered")

class Child():

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child before other altered()")
        self.other.altered()
        print("Child after other altered()")

son = Child()

son.implicit()
son.override()
son.altered()
