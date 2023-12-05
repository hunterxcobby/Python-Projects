#!/usr/bin/python3

# Set up gnureadline as readline if installed.
try:
    import gnureadline
    import sys
    sys.modules['readline'] = gnureadline
except ImportError:
    pass

    import cmd

    class Illustrate(cmd.Cmd):
        "Illustrate the base class method use."

        def cmdloop(self, intro=None):
            print('Welcome to the Airbnb Console!')
            return cmd.Cmd.cmdloop(self, intro)

        def preloop(self):
            print('Getting ready for Airbnb magic!')

        def postloop(self):
            print('Goodbye! Hope you enjoyed your Airbnb experience.')


        def parseline(self, line):
            print('Parsing the command: {!r}'.format(line), end='')
            ret = cmd.Cmd.parseline(self, line)
            print(ret)
            return ret
        
        def onecmd(self, s):
            print('Processing command: {}'.format(s))
            return cmd.Cmd.onecmd(self, s)

        def emptyline(self):
            print('You pressed enter without a command. Repeating previous command.')
            return cmd.Cmd.emptyline(self)

        def default(self, line):
            print('Command not recognized: {}'.format(line))
            return cmd.Cmd.default(self, line)

        def precmd(self, line):
            print('Preparing to execute: {}'.format(line))
            return cmd.Cmd.precmd(self, line)

        def postcmd(self, stop, line):
            print('Finished executing: {}'.format(line))
            return cmd.Cmd.postcmd(self, stop, line)

        def do_EOF(self, line):
            "Exit"
            return True


    if __name__ == '__main__':
        Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
