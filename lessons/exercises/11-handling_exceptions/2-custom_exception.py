#!/usr/bin/python3

"""Python allows you to define your own custom exceptions 
by creating new classes that inherit from 
the built-in Exception class."""


# Define a custom exception class called CustomError
# that inherits from the built-in Exception class.
class CustomError(Exception):
    pass # To pass the indentation error

# Define a function validate_input that takes a parameter x.
def validate_input(x):
    # Check if x is less than 0.
    if x < 0:
         # If x is less than 0, raise a CustomError
         #  with the message "Number must be positive".
        raise CustomError("Number must be positive")

# Use a try-except block to handle exceptions.
try:
     # Ask the user to input a number and convert it to an integer
    userInput = int(input("Enter a positive number: "))
    # Call the validate_input function to check the user's input.
    validate_input(userInput)

# If a CustomError is raised in the try block, catch it in the except block.
except CustomError as ce:
    # Print the message associated with the CustomError.
    print(ce)


