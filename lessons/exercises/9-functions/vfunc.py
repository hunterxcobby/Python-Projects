#!/usr/bin/python3

def greet_user(*args):# personal_profile(fname, lname, middle name, age.)
    # *arg => tuple
    print(args)

greet_user("Cobby", "Ami")


def greet_user(**kwargs):# personal_profile(fname, lname, middle name, age.)
    # **arg => dictionary
    print(kwargs)

greet_user()