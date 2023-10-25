#!/usr/bin/python3

"""Data encapsulation is the bundling of data (attributes)
and methods (functions) that operate on the data into a single unit 
or class. This unit restricts access to some of its components, 
providing a level of security for the data.
 It ensures that data is accessed and modified in a controlled manner."""

class Student:
    def __init__(self, name, age):
        self.name = name        # Public attribute
        self._age = age         # Protected attribute
        self.__grade = 'A'      # Private attribute

    def get_age(self):
        return self._age

    def set_grade(self, grade):
        self.__grade = grade

student = Student("John", 20)
print(student.name)     # Accessible
print(student._age)     # Accessible (though conventionally considered protected)
print(student.__grade)  # Error: 'Student' object has no attribute '__grade'


"""Benefits of Encapsulation:

Security: It provides a level of security by controlling access to certain data and methods. 
    Private data cannot be accessed directly from outside the class.
Flexibility and Modifiability: The internal representation of an object can be changed
    without affecting the external code that uses it. This is known as "information hiding."
Code Organization: It helps in organizing code by grouping related data and behavior together
    in a class."""