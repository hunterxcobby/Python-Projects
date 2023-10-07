#!/usr/bin/python3

#  provides an interface to various services
#  that interact with the system's underlying platform

import platform

x = platform.system() #operating system
print(x)

x = dir(platform) # list all the function names (or variable names) in a module.
print(x) 
    pass

import mymodules

x = dir(mymodules)
print(x)