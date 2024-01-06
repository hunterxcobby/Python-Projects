#!/usr/bin/python3

import cmd

class UserManagement(cmd.Cmd):
    """Simple CRUD command processor for managing users."""

    def __init__(self):
        super().__init__()
        self.users = {}  # Dictionary to store users

    def do_create(self, line):
        """Create a new user. Syntax: create <digit> <name>"""
        args = line.split()
        if len(args) == 2:
            digit, name = args
            self.users[digit] = name
            print(f"User created - ID: {digit}, Name: {name}")
        else:
            print("Invalid syntax. Use: create <digit> <name>")

    def do_read(self, line):
        """Read and display all users."""
        print("List of Users:")
        for digit, name in self.users.items():
            print(f"ID: {digit}, Name: {name}")
    



if __name__ == '__main__':
    UserManagement().cmdloop()

