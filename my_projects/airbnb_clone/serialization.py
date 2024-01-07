#!/usr/bin/python3

import json

"""
Suppose you have a dictionary representing your data, \
and you want to save it to a file in JSON format:"""

data = {
    "name" : "John",
    "age" : "21",
    "courses" : ["Maths", "History", "Computer Science"]
}

# serialize (convert to json formatted string)
json_string = json.dumps(data)

print(json_string)