#!/usr/bin/python3

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
