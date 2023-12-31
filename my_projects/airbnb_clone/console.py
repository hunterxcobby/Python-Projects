#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.basemodel import BaseModel
from models.user import User

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            object = self.CLASSES[class_name]()
            object.save()
            print(object.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])    

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def help_quit(self):
        print("Command to quit the program.")

    def default(self, line):
        """
        Handle unrecognized commands.
        """
        print(f"Unrecognized command: {line}. Type 'help' for assistance.")


if __name__ == '__main__':
    MyConsole().cmdloop()