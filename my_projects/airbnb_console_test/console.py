#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    def default(self, line):
        """Handle unrecognized commands."""
        print(f"Unrecognized command: {line}. Type 'help' for assistance.\n")

    def do_create(self, line):
        """Creates a new instance of a specified class."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        
        try:
            object = BaseModel()
            object.save()
            print(object.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])


    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.all().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        args = line.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        elif args[0] not in storage.all().keys():
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                class_name = key.split('.')[0]
                if class_name == args[0]:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.all().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = storage.all()[obj_key]
            attr_name = args[2]
            attr_value_str = args[3]

            # Handling values in double quotes
            if attr_value_str.startswith('"') and attr_value_str.endswith('"'):
                attr_value = attr_value_str[1:-1]
            else:
                attr_value = attr_value_str

            # Get the attribute type from the object's class
            attr_type = type(getattr(obj, attr_name, None))

            # Cast the attribute value to the correct type
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(f"Value {attr_value} cannot be casted to type {attr_type}")
                return

            # Update the attribute and save changes
            setattr(obj, attr_name, attr_value)
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
