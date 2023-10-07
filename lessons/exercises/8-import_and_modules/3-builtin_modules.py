#!/usr/bin/python3

#  provides an interface to various services
#  that interact with the system's underlying platform

import platform

x = platform.system() #operating system
print(x)

x = dir(platform)
print(x) 