#!/usr/local/bin/python3
'''
LPTHW exercise 44c
Alter Before and After
'''

class Parent():

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def aleterd(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.aleterd()
