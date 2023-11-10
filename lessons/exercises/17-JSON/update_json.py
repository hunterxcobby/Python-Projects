#!/usr/bin/python3

import json

# let us write our function for writing into the json file
def write_json(data, filename="profile.json"):
    """
    Writes the given data to a JSON file.

    Args:
        data (dict): The data to be written to the file.
        filename (str): The name of the file. Default is "user2.json".
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


with open("profile.json") as json_file:
    data = json.load(json_file)
    temp = data["profile"]
    update = {"name" : "Sena",
              "age":26,
              "profession": "student"}

    temp.append(update)

write_json(data)