#!/usr/bin/python3

def infoperson(*args, **kwargs):
    for key,value in kwargs.items(): #we need to use this method since it creates a dict
        print(key,value, sep=": ")
    
    for i in args:
        print(i, end=": ")
    print()

# remember that the arbituary position arg comes before the keyword in the function
infoperson(12, 3, 4,name="Cobby", age=21, dept="CSE")
infoperson(54, 15, 89,name="Ami", age=20, dept="CSE")
