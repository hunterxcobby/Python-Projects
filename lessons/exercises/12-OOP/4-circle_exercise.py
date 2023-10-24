#!/usr/bin/python3

class Circle:
    pi = 3.14
    def __init__(self, radius, diameter=0):
        self.radius = radius
        self.diameter = diameter

    def circumference(self):
        circum = 2 * self.pi * self.radius
        return circum
    
    def area(self):
        a = self.pi * (self.radius ** 2)
        return a

circle_1 = Circle(4)
print(circle_1.circumference())
print(circle_1.area())


circle_2 = Circle(14)
print(circle_2.circumference())


