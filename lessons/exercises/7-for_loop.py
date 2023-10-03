#!/usr/bin/python3

"""Prints each character in a string"""

f_name = input("first name:")

for c in f_name:
    print(c)

l_name = input("Surname:")

for c in l_name:
    if (c == "e"):
        continue
    print(c*3)