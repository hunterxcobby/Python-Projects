#!/usr/bin/python3

import cmd

""""
We will use this to work on our CRUB operations"""

class command(cmd.Cmd): #a Cmd class inheriting from the cmd mod
    """THis is a simple command line processor"""

    prompt = "(HBNB)"
    
    def do_greet(self, person):
        # """greet [person]
        # Greet the name person"""
        if person:
            print("HI,", person)
        else:
            print("HI")

    def help_greet(self):
        print('\n'.join([
            'greet [person]',
            'Greet the named person',
        ]))
    
    def do_EOF(self, line): #sub class handle end of file marker
        """Exit the console successfully"""
        print()
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program."""
        return True
    
    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    
    def default(self, line): # when we reive an unknown command
        """in case the user enters the wrong command"""
        print(f"Unknown command: {line}")

    def emptyline(self):
        """Overwrite the empty line method"""
        print("YOu entered an empty line")
        return super().emptyline()
    

if __name__ == '__main__': #command python idiom to check if script is main program
    command().cmdloop() #basically to capture the user in the loop.


"""So this is our console app working as it is supposed to
but we have a problem when exiting, or when the user enters the wrong command"""