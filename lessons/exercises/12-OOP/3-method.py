#!/usr/bin/python3

class Instructor:
    followers = 0 # Class Object variable

    def __init__(self, name, address):
        self.name=name
        self.address=address
        
    # defining a method
    def display(self, subject_name):
        print(f"{self.name} teaches {subject_name}")

    # define another method
    def update_followers(self, follower_name):
        self.followers += 1
        print(f"{follower_name} followed {self.name}")

instructor_1=Instructor("Cobby","Accra")
print(f"{instructor_1.name} is from {instructor_1.address}")
instructor_1.display("Computer Science")
print(f"{instructor_1.name} has {instructor_1.followers} followers")
instructor_1.update_followers("Kwesi")
print(f"{instructor_1.name} has {instructor_1.followers} followers now")


instructor_2 = Instructor("Kwesi", "Tema")
print(f"{instructor_2.name} is from {instructor_2.address}")
instructor_2.display("Pharmacy")
print(f"{instructor_2.name} has {instructor_2.followers} followers")

instructor_3 = Instructor("Kelvin", "Legon")
print(f"{instructor_3.name} is from {instructor_3.address}")
instructor_3.display("Pharmacy")
print(f"{instructor_3.name} has {instructor_3.followers} followers")

