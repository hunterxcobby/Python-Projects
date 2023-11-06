#!/usr/bin/python3

"""Inheritance helps us reuse code and organize it better. 
Instead of writing the same code over and over for different classes, 
we can create a common base class and then create specialized 
subclasses that inherit from it.

It's like having a general blueprint for a robot (the parent class) 
and then making specific types of robots (the subclasses) based on that blueprint. 
This way, if we make a change to the blueprint, 
it automatically applies to all the specific types of robots.

Inheritance also helps create a hierarchy in our code. 
It allows us to represent real-world relationships between objects. 
For example, a Vehicle class can be a parent to Car, Bike, and Truck subclasses, 
because all of them share some common features like wheels and movement."""

class Vehicle:
    def move(self):
        print("I can move")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

car = Car()
car.move()  # This will print "I can move"


'''In this example, Car, Bike, and Truck inherit the move method from the Vehicle class. 
They all share the ability to move, 
but they can have their own unique features too.
'''