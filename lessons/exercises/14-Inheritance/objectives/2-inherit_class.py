#!/usr/bin/python3

class BasicRobot:
    def walk(self):
        print("I can walk")

    def talk(self):
        print("I can talk")

class SpecialRobot(BasicRobot):
    def fly(self):
        print("I can jump")

    def swim(self):
        print("I can swim")

special_robot = SpecialRobot()
special_robot.walk()
special_robot.talk()
special_robot.fly()
special_robot.swim()
