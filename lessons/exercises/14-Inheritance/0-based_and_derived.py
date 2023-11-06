#!/usr/bin/python3

# We create a class
class Humans: #Super||Base||Parent class

    # We give this class some methods
    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")
    
class males(Humans): # Sub||Derived||Child class
    def drive(self):
        print("I can drive") # Its own method
    def work(self):
        print("I can work very hard")# This is called overriding

cobby = males()
cobby.eat() # Inherit from the parent method
cobby.drive() #its own method
cobby.work() # override the parents method
