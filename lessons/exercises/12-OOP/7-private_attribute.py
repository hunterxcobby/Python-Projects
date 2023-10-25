#!/usr/bin/python3

"""A private attribute is one that should not be accessed directly
from outside the class. 
    It is indicated by two underscores before the attribute's name.
    However, it's worth noting that Python uses name mangling 
    to make it harder to access private attributes, but it is still possible.
Example:"""

class Car:
    def __init__(self, make, model):
        self.__make = make   # Private attribute
        self.__model = model # Private attribute

my_car = Car("Toyota", "Camry")
# print(my_car.__make) # This will cause an error (AttributeError)