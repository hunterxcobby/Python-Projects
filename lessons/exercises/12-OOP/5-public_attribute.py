#!/usr/bin/python3

class Car:
    def __init__(self, make, model):
        self.make = make   # Public attribute
        self.model = model # Public attribute

my_car = Car("Toyota", "Camry")
print(my_car.make)   # Accessing public attribute
print(my_car.model)