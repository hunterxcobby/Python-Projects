#!/usr/bin/python3

"""A protected attribute is one that is intended
to be used only within the class and 
its subclasses (but not outside). It is indicated 
by a single underscore before the attribute's name.
Example:"""

class Car:
    def __init__(self, make, model):
        self.make = make   # Public attribute
        self.model = model # Public attribute

my_car = Car("Toyota", "Camry")
print(my_car.make)   # Accessing public attribute
print(my_car.model)