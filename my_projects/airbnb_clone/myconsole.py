#!/usr/bin/python3

import cmd

""""
We will use this to work on our CRUB operations"""

class command(cmd.Cmd): #a Cmd class inheriting from the cmd mod
    """THis is a simple command line processor"""

    def do_greet(self, line):
        print("Hello world")
    """the first parameter of a method is conventionally named self
      and refers to the instance of the class. 
      The line parameter is used to capture the user input provided after the command."""
    
if __name__ == '__main__': #command python idiom to check if script is main program
    command().cmdloop() #basically to capture the user in the loop.

"""So this is our console app working as it is supposed to
but we have a problem when exiting, or when the user enters the wrong command"""