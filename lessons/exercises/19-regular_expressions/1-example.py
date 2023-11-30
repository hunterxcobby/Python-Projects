#!/usr/bin/env python3

import re

email = input("What is your email?").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")