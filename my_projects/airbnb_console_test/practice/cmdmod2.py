#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print("hello")
    
    def do_EOF(self, line):
        print() #to print a newline before exiting
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
