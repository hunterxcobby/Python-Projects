#!/usr/bin/python3

#Asks user for name and saves it in a variable
name = input("What is your name? ")

#prints users name to screen
print(f"{name}", end=" ")

#save the string length of name and save it in a variable
length = len(name)

#prints the length of the user's name
print(f"your name is {length} characters long")