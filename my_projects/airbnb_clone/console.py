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


if __name__ == '__main__':
    UserManagement().cmdloop()

"""
This is the constructor method (__init__) of the class.
It is automatically called when an instance of the class is created."""

"""
super().__init__(): This line calls the constructor of the superclass (cmd.Cmd in this case).
It's essential to call the constructor of the superclass
to ensure that the necessary initialization from the parent class is performed."""

"""
for the create
Certainly, let's break down the `do_create` method:

```python
def do_create(self, line):
    """Create a new user. Syntax: create <digit> <name>"""
    args = line.split()
    if len(args) == 2:
        digit, name = args
        self.users[digit] = name
        print(f"User created - ID: {digit}, Name: {name}")
    else:
        print("Invalid syntax. Use: create <digit> <name>")
```

1. **Method Signature:** `def do_create(self, line):` - This line defines the `do_create` method. In the context of the `cmd` module, methods starting with "do_" are associated with commands that the user can enter in the command-line interface.

2. **Docstring:** `"""Create a new user. Syntax: create <digit> <name>"""` - This is a docstring providing a brief description of what the `do_create` method does. It also includes information about the expected syntax for using the `create` command.

3. **Parsing the Input:** `args = line.split()` - It splits the user input (`line`) into a list of words. For example, if the user enters "create 1 John," `args` will be `['create', '1', 'John']`.

4. **Input Validation:** `if len(args) == 2:` - Checks if the user has provided exactly two arguments after the "create" command. In this case, the expected arguments are the digit (ID) and the name.

5. **Extracting Values:** `digit, name = args` - If the input is valid, it extracts the digit and name from the `args` list.

6. **Updating the Dictionary:** `self.users[digit] = name` - Adds a new entry to the `users` dictionary, where the digit is the key and the name is the value.

7. **User Feedback:** `print(f"User created - ID: {digit}, Name: {name}")` - Prints a confirmation message indicating that the user has been created with the specified ID and name.

8. **Invalid Syntax Handling:** `else: print("Invalid syntax. Use: create <digit> <name>")` - If the input is not valid (i.e., the user did not provide exactly two arguments), it prints an error message indicating the correct syntax for using the `create` command.

In summary, the `do_create` method handles the "create" command, validates the input, updates the `users` dictionary, and provides feedback to the user.
"""