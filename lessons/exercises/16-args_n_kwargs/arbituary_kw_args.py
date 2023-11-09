#!/usr/bin/python3

# Defining a function named 'infoperson' that accepts a variable number of positional arguments (*args)
# and a variable number of keyword arguments (**kwargs).
def infoperson(*args, **kwargs):
    # Loop through the keyword arguments and print each key-value pair.
    for key, value in kwargs.items(): #we need to use this method since it creates a dict
        print(key, value, sep=": ")
    
    # Loop through the positional arguments and print each value.
    for i in args:
        print(i, end=": ")
    print()

# Calling the 'infoperson' function with a combination of positional and keyword arguments.
# remember that the arbituary position arg comes before the keyword in the function
infoperson(12, 3, 4, name="Cobby", age=21, dept="CSE")
infoperson(54, 15, 89, name="Ami", age=20, dept="CSE")
