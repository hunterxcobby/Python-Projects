#!/usr/bin/python3

class Student:
    def __init__(self, name, rollno, age):
        self.name = name # Public Instance Variable
        self._rollno = rollno #Protected Instance Variable
        self.__age = age #Private Instance Variable
    
    def __display(self):
        print(f"My name is {self.name} on rollno {self._rollno} from student class")
    def dislayPrivateData(self):
        print(f"My name is {self.name}, I am {self.__age} years old and on rollno {self._rollno} from student class")

class Branch(Student): # we use this class for protected data
    def show(self):
        print(f"My rollno is {self._rollno}")

b1 = Branch("Ami", 45, 20)
b1.show()

# def showdata():
#     b1 = Branch("Nisha", 45)
#     print(b1.name)
#
# showData()
s1 = Student("Cobby", 46, 21)
#print(s1.__age)
# print(s1.name)
#self.display()
s1.dislayPrivateData()
#print(dir(s1)) # BShow all the valid attributes of the object s1
print(s1._Student__age) # using name mangling to acces a private attribute 
s1._Student__display() # using name mangling to acces a private methods




