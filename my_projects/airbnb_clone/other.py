import json
import cmd
import uuid
from datetime import datetime

class UserManagement(cmd.Cmd):
    """Simple CRUD command processor for managing users."""

    def __init__(self):
        super().__init__()
        self.users = {}  # Dictionary to store users
        self.load_from_file()

    def do_create(self, line):
        """Create a new user. Syntax: create <name>"""
        name = line.strip()
        if name:
            user_id = str(uuid.uuid4())
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_data = {"name": name, "created_at": created_at, "updated_at": created_at}
            self.users[user_id] = user_data
            print(f"User created - ID: {user_id}, Name: {name}")
        else:
            print("Invalid syntax. Use: create <name>")
        self.save_to_file()

    def do_read(self, line):
        """Read and display all users."""
        print("List of Users:")
        for user_id, user_data in self.users.items():
            print(f"ID: {user_id}, Name: {user_data['name']}, Created At: {user_data['created_at']}, Updated At: {user_data['updated_at']}")

    def do_update(self, line):
        """Update user's name. Syntax: update <user_id> <new_name>"""
        args = line.split()
        if len(args) == 2:
            user_id, new_name = args
            if user_id in self.users:
                updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.users[user_id]["name"] = new_name
                self.users[user_id]["updated_at"] = updated_at
                print(f"User updated - ID: {user_id}, New Name: {new_name}")
            else:
                print(f"No user found with ID {user_id}")
        else:
            print("Invalid syntax. Use: update <user_id> <new_name>")
        self.save_to_file()

    def do_destroy(self, line):
        """Delete a user by ID. Syntax: destroy <user_id>"""
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
    UserManagement().cmdloop()
