#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
from models import storage
import re


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
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
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
        """Prints the string representation of an instance
        based on the class name and id."""
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
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
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
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if key.startswith(args[0] + '.')])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** class name missing **")
            return

        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if classname not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        elif uid is None:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
                return
            elif not attribute:
                print("** attribute name missing **")
                return
            elif not value:
                print("** value missing **")
                return
            else:
                obj = storage.all()[key]
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = {k: type(v) for k, v in obj.to_dict().items()}
                if attribute not in attributes:
                    # Attribute doesn't exist, create it with the given value
                    setattr(obj, attribute, value)
                    storage.save()
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        print(f"Value {value} cannot be casted to type {cast}")
                        return
                    setattr(obj, attribute, value)
                    storage.save()
                else:
                    # Update the attribute with the given value
                    setattr(obj, attribute, value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
