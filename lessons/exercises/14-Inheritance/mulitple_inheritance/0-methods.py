#!/usr/bin/python3


class Human:
    
    def eat(self):
        print("I can eat")

    def work(self):
        print('I can work')

class Male:

    def work(self):
        print("I can work very well")
    
    def drive(self):
        print("I can drive")


class Boy(Human, Male):
    
    def work(self):
        print("I can run!")

boy_1 = Boy()
boy_1.eat()
boy_1.work()
boy_1.drive()
Human.work(boy_1)
Male.work(boy_1) # this is to specify the class to inherit from if not first parent passed to it
print(Boy.mro()) # the order of method resolutiom



