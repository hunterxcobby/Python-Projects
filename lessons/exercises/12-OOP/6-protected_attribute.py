#!/usr/bin/python3

"""A protected attribute is one that is intended
to be used only within the class and its subclasses (but not outside). 
 It is indicated by a single underscore before the attribute's name."""

class Car:
    def __init__(self, make, model):
        self._make = make   # Protected attribute
        self._model = model # Protected attribute

my_car = Car("Toyota", "Camry")
print(my_car._make)   # Accessing protected attribute