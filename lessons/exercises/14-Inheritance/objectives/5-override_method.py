#!/usr/bin/python3

"""Imagine you have a robot that can talk, 
but you want your special robot to talk in a cooler way. 
You can change the way it talks by writing your own 
version of the talk method.

Python allows you to do this by overriding the method. 
This means you provide a new definition for the method 
in your special robot. When you call the talk method 
on your special robot, it uses your custom version 
instead of the default one.
"""
class SimpleRobot:
    def talk(self):
        print("I can talk")

class SpecialRobot(SimpleRobot):
    def talk(self):  # We're redefining the 'talk' method here.
        print("I can talk in a special way!")

simple_robot = SimpleRobot()
simple_robot.talk()
special_robot = SpecialRobot()
special_robot.talk()  # This will print "I can talk in a special way!"

