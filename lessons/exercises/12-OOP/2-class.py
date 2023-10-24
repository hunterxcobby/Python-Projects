#!/usr/bin/python3

class Instructor:
    def __init__(self, name, address):
        self.name=name
        self.address=address
        self.followers = 0

instructor_1=Instructor("Cobby","Accra")
print(instructor_1.name)
print(instructor_1.address)
print(instructor_1.followers)

instructor_2 =  Instructor("Kwesi", "Tema")
instructor_3 = Instructor("Kelvin", "Legon")