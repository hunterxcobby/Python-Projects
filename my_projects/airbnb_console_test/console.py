#!/usr/bin/env python3
import cmd 

class myConsole(cmd.Cmd):
    prompt = "cmd$ "
    pass

if __name__ == '__main__':
    myConsole().cmdloop()