#!/usr/bin/python3

# The "and" keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 50
c = 300
if a > b and c > a:
    print("Both conditions are true")

# The or keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 300
c = 50
if a > b or a > c:
    print("At least one of the conditons is true")