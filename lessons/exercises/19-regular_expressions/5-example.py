#!/usr/bin/env python3

import re

email = input("What is your email?").strip()

if re.search(r"^[^@]+@[^@]\.edu$", email):
    print("Valid")
else:
    print("Invalid")