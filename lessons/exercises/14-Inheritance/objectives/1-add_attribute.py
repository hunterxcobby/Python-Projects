#!/usr/bin/python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

john = Person("John Doe", 25)

# Adding a new attribute to the instance 'john'
john.location = "New York"

print(john.name)  # Output: John Doe
print(john.age)   # Output: 25
print(john.location)  # Output: New York

# Think of an instance like a specific robot made from the blueprint. 
# This robot might have a name, a color, and can do some things.
# Sometimes, after making the robot, you realize you want to give it a special power or 
# add something new to it. For example, maybe you want to give it the ability to fly.
# Python allows you to do this! You can give the robot new features even after it's been made.