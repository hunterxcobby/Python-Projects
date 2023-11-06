#!/usr/bin/python3

"""isinstance:
is a built-in function in Python that helps you check 
if an object belongs to a particular class or type."""

num = 5
if isinstance(num, int):
    print("It's an integer")
else:
    print("It is not an integer")



"""issubclass:
is a built-in function that helps you check 
if a class is a subclass of another class."""

class Vehicle:
    pass

class Car(Vehicle):
    pass

if issubclass(Car, Vehicle):
    print("Car is a subclass of Vehicle")



"""type:
is a built-in function that tells you the type of an object."""

num = 5
print(type(num))  # This will print "<class 'int'>"



"""super:
is used to refer to the parent class in a class hierarchy. 
It's particularly useful when you're working with inheritance 
and want to call methods from the parent class."""

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Calls the make_sound method from the parent class
        print("Bark")

husky = Dog()
husky.make_sound()