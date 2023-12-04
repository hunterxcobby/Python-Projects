#!/usr/bin/env python3
import cmd 

class myConsole(cmd.Cmd):
    prompt = "cmd$ "
    
    def do_create(self, input):
        print("I have created",input)

    def do_exit(self, ):
        exit()

if __name__ == '__main__':
    myConsole().cmdloop()