#!/usr/bin/python3

'''The finally block is used in conjunction with a try block 
and it always executes, regardless of whether an exception
was raised or not.
It is typically used to perform cleanup actions
like closing files or releasing resources.'''

# Open a file named "example.txt"
try:
    file = open("example.txt", "r")# Try to open the file in read mode
    content= file.read() # Read the content of the file
except FileNotFoundError:
    print("File not found, creating a new file ...")
    # Open the file in write mode 
    # (which creates it if it doesn't exist)
    file = open("example.txt", "w")
    file.write("This is a text on newline.\n")
finally: # everything thing under this block of code will run
    file.close() # Ensure the file is closed, whether an exception occurred or not