#!/usr/bin/python3

"""This is to illustrate the use of getters and setters method 
to access a private class attribute
This method helps us avoid direct access to the private attributes """

class Student:
    def __init__(self, name, rollno, age):
        self.name = name # Public Instance Variable
        self._rollno = rollno #Protected Instance Variable
        self.__age = age #Private Instance Variable
    
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 27:
            print("Invalid age, less should be less than 27")
        else:
            self.__age = age

    def __display(self):
        print(f"My name is {self.name} on rollno {self._rollno} from student class")
    def dislayPrivateData(self):
        print(f"My name is {self.name}, I am {self.__age} years old and on rollno {self._rollno} from student class")

s1 = Student("Cobby", 45, 20)
print(s1.get_age())
s1.set_age(22)
print(s1.get_age())


# s1 = Student("Cobby", 45, 20)
# print(s1._Student__age)
# s1._Student__age = 21
# s1._Student__display()
