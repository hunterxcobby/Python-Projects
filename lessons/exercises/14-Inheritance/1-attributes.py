#!/usr/bin/python3

# Define a class named Humans
class Humans: #Base || Super || Child Class

    def __init__(self, heart):
        self.eyes = 2
        self.nose = 1
        self.heart = heart

    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")

# Define a class named males that inherits from Humans
class males(Humans): #Derived || Sub || Child Class

    def __init__(self, age, heart):
        super().__init__(heart) # We need to use the super function for the age attirbute
        self.age = age

    def drive(self):
        print("I can drive")

    def work(self):
        super().work()  
        print("I can work very hard") 

cobby = males(21, 1)
print(f"Cobby has {cobby.eyes} eyes ")
print(f"Cobby is  {cobby.age} years old")
print(f"Cobby has {cobby.heart} heart ")

