#!/usr/bin/python3

# Define a class named Humans
class Humans: #Base || Super || Child Class

    # Define a method named eat within the Humans class
    def eat(self):
        print("I can eat")
    
    # Define a method named work within the Humans class
    def work(self):
        print("I can work")

# Define a class named males that inherits from Humans
class males(Humans): #Derived || Sub || Child Class

    # Define a method named drive within the males class
    def drive(self):
        print("I can drive")
    
    # Override the work method from the parent class Humans
    def work(self):
        super().work()  # Call the work method from the parent class
        print("I can work very hard") # override the parents implementation

# Create an instance of the males class named cobby
cobby = males()

# Call the eat method for the instance cobby
cobby.eat() 

# Call the drive method for the instance cobby
cobby.drive()

# Call the work method for the instance cobby
cobby.work()
