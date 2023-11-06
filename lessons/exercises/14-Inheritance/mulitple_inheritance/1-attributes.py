#!/usr/bin/python3


class Human:
    print("Calling int from human")

    def __init__(self, heart):
        self.eyes = 2
        self.nose = 1
        self.heart = heart

    def eat(self):
        print("I can eat")

    def work(self):
        print('I can work')

class Male:
    print("Calling int from Male")

    def __init__(self, name):
        self.name = name
    
    def work(self):
        print("I can work very well")
    
    def drive(self):
        print("I can drive")


class Boy(Human, Male):
    
    def __init__(self, name, heart,language):
        Human.__init__(self,heart)
        Male.__init__(self, name)
        self.language = language

    def work(self):
        print("I can run!")


boy_1 = Boy("Cobby", 1, "Python")
print(f"I have one {boy_1.nose} nose")
print(f"I have two {boy_1.eyes} eyes ")
print(f"My name is {boy_1.name} and I code in {boy_1.language} language")
# print(f"My name is {Male.name(boy_1)} ")


