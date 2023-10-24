#!/usr/bin/python3

# Step 1: Define a class named 'Person'.
class Person:
    total_persons = 0  # This is a class variable

    # Step 2: Initialize the class.
    def __init__(self, name, age):
        # Step 3: Define instance variables 'name' and 'age'.
        self.name = name
        self.age = age
        Person.total_persons += 1 # Increment total_persons each time a new Person is created

    # Step 4: Define a method 'introduce'.
    def introduce(self):
        # Step 5: Print a formatted string using instance variables.
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")

# Step 6: Create an instance of the class.
john = Person("Cobby", 21)

# Step 7: Call the 'introduce' method of the object.
john.introduce()
