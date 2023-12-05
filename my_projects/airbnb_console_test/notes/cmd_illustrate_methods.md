### Overriding Base Class Methods:

#### 1. **Overview:**
   - The example illustrates how to override various base class methods in the `cmd` module to customize the behavior of the command interpreter.

#### 2. **Commonly Useful Methods:**
   - The example overrides methods such as `cmdloop`, `preloop`, `postloop`, `parseline`, `onecmd`, `emptyline`, `default`, `precmd`, and `postcmd`.

#### 3. **Example Code:**
   ```python
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
           print('cmdloop({})'.format(intro))
           return cmd.Cmd.cmdloop(self, intro)

       def preloop(self):
           print('preloop()')

       def postloop(self):
           print('postloop()')

       def parseline(self, line):
           print('parseline({!r}) =>'.format(line), end='')
           ret = cmd.Cmd.parseline(self, line)
           print(ret)
           return ret

       def onecmd(self, s):
           print('onecmd({})'.format(s))
           return cmd.Cmd.onecmd(self, s)

       def emptyline(self):
           print('emptyline()')
           return cmd.Cmd.emptyline(self)

       def default(self, line):
           print('default({})'.format(line))
           return cmd.Cmd.default(self, line)

       def precmd(self, line):
           print('precmd({})'.format(line))
           return cmd.Cmd.precmd(self, line)

       def postcmd(self, stop, line):
           print('postcmd({}, {})'.format(stop, line))
           return cmd.Cmd.postcmd(self, stop, line)

       def do_greet(self, line):
           print('hello,', line)

       def do_EOF(self, line):
           "Exit"
           return True


   if __name__ == '__main__':
       Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
