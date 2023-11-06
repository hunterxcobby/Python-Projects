#!/usr/bin/python3

class MyClass:
    def __init__(self):
        self.attribute1 = 10
        self.attribute2 = "Hello"
    def method1(self):
        pass
    def method2(self):
        pass

instance = MyClass()

print(dir(instance))  # Output will list all attributes and methods of 'instance'

"""Imagine you have a class. 
A class is like a blueprint that helps create objects. 
An object is like a thing that follows the rules in the blueprint.
Now, sometimes you might want to see all the things (attributes) 
and actions (methods) that an object can do. 
It's like having a list of what a robot can do - walk, talk, etc.
Python lets you see this list. 
You can ask Python to show you all the things and actions that an object can have. 
This is useful to understand what you can do with that object."""