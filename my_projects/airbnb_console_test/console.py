#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True


    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command"""
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def default(self, line):
        """
        Handle unrecognized commands.
        """
        print(f"Unrecognized command: {line}. Type 'help' for assistance.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()