#!/usr/bin/python3

import json

file = "user.json"

with open(file, "r") as json_file:
    data = json.load(json_file)# this is where the magic starts

    print(data["name"])
    name = data["name"]
    age = data['Age']
    hobbies = data['Hobbies']
    print(f"{name} is {age} years old and his hobbies are", end=" ")

    for hobbies in data['Hobbies']:
        print(hobbies, end=", ")
    print()
    for friends in data["Friends"]:
        print(f"{data['name']} and {friends['name']} are best friends " )
        sub_friends = friends['Friends'][1]
        print(f"{friends['name']} and {sub_friends} are friends " )
    



