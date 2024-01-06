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
    
    def do_update(self, line):
        """Update user's name. Syntax: update <digit> <new_name>"""
        args = line.split()
        if len(args) == 2:
            digit, new_name = args
            if digit in self.users:
                self.users[digit] = new_name
                print(f"User updated - ID: {digit}, New Name: {new_name}")
            else:
                print(f"No user found with ID {digit}")
        else:
            print("Invalid syntax. Use: update <digit> <new_name>")

if __name__ == '__main__':
    UserManagement().cmdloop()

"""
Method Signature: def do_update(self, line): - This line defines the do_update method, associated with the "update" command.


Parsing the Input: args = line.split() - Splits the user input (line) into a list of words. For example, if the user enters "update 1 JohnDoe," args will be ['update', '1', 'JohnDoe'].

Input Validation: if len(args) == 2: - Checks if the user has provided exactly two arguments after the "update" command, which are the digit (ID) and the new name.

Extracting Values: digit, new_name = args - If the input is valid, it extracts the digit and new name from the args list.

Checking User Existence: if digit in self.users: - Verifies if a user with the specified digit (ID) exists in the users dictionary.

Updating the Dictionary: self.users[digit] = new_name - If the user exists, it updates the user's name with the new name.

User Feedback: print(f"User updated - ID: {digit}, New Name: {new_name}") - Prints a confirmation message indicating that the user has been updated with the specified ID and new name.

User Not Found Handling: else: print(f"No user found with ID {digit}") - If the user with the specified digit is not found, it prints an error message indicating that no user was found with that ID.

Invalid Syntax Handling: else: print("Invalid syntax. Use: update <digit> <new_name>") - If the input is not valid, it prints an error message indicating the correct syntax for using the "update" command.

In summary, the do_update method handles the "update" command, validates the input, updates the user's name if the user exists, and provides feedback to the user. If the user does not exist, it informs the user accordingly."""