#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command"""
        print("Exiting the console...")
        return True

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def help_quit(self):
        print("Command to quit the program.")

if __name__ == '__main__':
    MyConsole().cmdloop()