#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
import sys


class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_EOF(self, line):
        """Exit the console on EOF (Ctrl+D) command"""
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


"""Non-interactive mode.
To run our console in non-interactive mode
"""


def run_console():
    console = MyConsole()

    if not sys.stdin.isatty():
        # Read commands from standard input in non-interactive mode
        for line in sys.stdin:
            console.onecmd(line.strip())

    else:
        # Run the console interactively
        console.cmdloop()


if __name__ == '__main__':
    run_console()
