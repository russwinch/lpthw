#!/usr/local/bin/python3
'''
LPTHW exercise 42
Objects and Classes
'''

class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Owner():
    def __init__(self, name):
        self.name = name
        self.pet = None

rover = Dog("Rover")
shredder = Cat("Shredder")

russ = Owner("Russ")

russ.pet = rover

print(rover.name)
print(russ.pet.name)
