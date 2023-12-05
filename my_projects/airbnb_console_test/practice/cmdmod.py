#!/usr/bin/python3

import cmd

class MyCmd(cmd.Cmd):
    def do_hello(self, arg):
        print(arg)
        print("hello")
        print("Hello,", arg)

if __name__ == "__main__":
    my_cmd_instance = MyCmd()
    my_cmd_instance.cmdloop()
