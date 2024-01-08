#!/usr/bin/python3

import json

#load from file
with open("data.json", "r") as json_file:
    json_string = json_file.read()

# Deserialize (convert from JSON-formatted string to dictionary)
data = json.loads(json_string)

# Use the data as a Python dictionary
print(data["name"])
print(data["age"])
print(data["courses"])

