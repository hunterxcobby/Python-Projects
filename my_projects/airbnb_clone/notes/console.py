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

    def load_from_file(self):
        """Load user data from a JSON file."""
        try:
            with open("user_data.json", "r") as json_file:
                self.users = json.load(json_file)
        except FileNotFoundError:
            print("No user data file found. Starting with an empty user dictionary.")

if __name__ == '__main__':
    UserManagement.load_from_file()
    UserManagement().cmdloop()

"""
The `user_management.load_from_file()` call is done for a specific purpose: to initialize the `self.users` dictionary with any existing user data stored in a JSON file. Let me explain why this is important:

1. **Persisting User Data:**
   - When users are created, updated, or deleted using your `UserManagement` class, the changes are made to the `self.users` dictionary in memory.
   - However, these changes are temporary while the program is running. If the program is closed or restarted, the in-memory data will be lost.

2. **Loading Data from a File:**
   - By calling `load_from_file` at the beginning of your program, you're attempting to load any previously saved user data from a JSON file into the program's memory.
   - This ensures that the `self.users` dictionary starts with the latest data that was saved in previous program sessions.

3. **Persistence Across Sessions:**
   - With the `load_from_file` method, your program becomes more persistent. It can remember and work with data from previous sessions rather than starting fresh each time it runs.
   - This is useful in scenarios where you want your program to remember user data between different runs or sessions.

4. **Consistency and Data Integrity:**
   - If you only work with an in-memory dictionary and don't save/load data to/from a file, your program won't maintain consistency across multiple runs.
   - By loading data from a file at the beginning, you ensure that the program starts with a consistent and updated state.

In summary, calling `user_management.load_from_file()` is a strategy to make your program more robust and persistent by loading any existing user data from a file into the program's memory, providing continuity and consistency across different runs of the program."""

