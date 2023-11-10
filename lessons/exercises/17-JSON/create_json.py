#!/usr/bin/python3

import json




# Let us write a function that will put the data into a json file
def write_json(data, filename= "user2.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

file_from = "user.json"

with open(file_from, "r") as json_file:
    data = json.load(json_file)# this is where the magic starts

write_json(data)