#!/usr/bin/python3

''' This is to explain the concept of Exception Handling'''
# This refers to the errors one faces when they try to run the progtram
# When something goes wrong while your program is running, we call it an "exception"
# It's like your program saying, "Hey, something unexpected just happened!"

# We can write a program to handle some of these exeptions
# Using the try except statement

while True:
    try:
        int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

'''
    In this code we expect a user to enter a number 
    this is done in the try block and when the user 
    enters a value that is not a number, we handle it 
    with the except block that raises a valueerror
    this is a fundamental code to explain an Exception handling
'''