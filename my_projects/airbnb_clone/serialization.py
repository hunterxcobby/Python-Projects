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

# save it to a file
with open("data.json","w") as json_file:
    json_file.write(json_string)


"""
 It's commonly used for configuration files, data exchange between a server and a web application, and more.
 In the context of file storage, you can use JSON to serialize (convert to a string) and deserialize (convert back to a Python object) data."""

