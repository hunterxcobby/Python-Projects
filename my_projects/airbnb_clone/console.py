#!/usr/bin/python3

import cmd
import json

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
        self.save_to_file()

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
        self.save_to_file()

    def do_destroy(self, line):
        """Delete a user by ID. Syntax: destroy <digit>"""
        if line in self.users:
            del self.users[line]
            print(f"User deleted - ID: {line}")
        else:
            print(f"No user found with ID {line}")
        self.save_to_file()

    def save_to_file(self):
        """Save user data to a JSON file."""
        with open("user_data.json", "w") as json_file:
            json.dump(self.users, json_file)

if __name__ == '__main__':
    UserManagement().cmdloop()

"""
Method Signature: def do_destroy(self, line): - This line defines the do_destroy method, associated with the "destroy" command.


User Input: if line in self.users: - Checks if the user input (line) corresponds to an existing user ID in the users dictionary.

Deleting User: del self.users[line] - If the user ID exists, it deletes the corresponding user from the users dictionary.

User Feedback: print(f"User deleted - ID: {line}") - Prints a confirmation message indicating that the user with the specified ID has been deleted.

User Not Found Handling: else: print(f"No user found with ID {line}") - If the user with the specified ID is not found, it prints an error message indicating that no user was found with that ID.

In summary, the do_destroy method handles the "destroy" command, checks if the specified user ID exists, deletes the user if found, and provides feedback to the user. If the user ID is not found, it informs the user accordingly."""

