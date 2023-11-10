#!/usr/bin/python3

import json

# Function to write data to a JSON file with indentation
def write_json(data, filename="user2.json"):
    """
    Writes the given data to a JSON file.

    Args:
        data (dict): The data to be written to the file.
        filename (str): The name of the file. Default is "user2.json".
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Source JSON file
file_from = "user.json"

# Read data from the source file
with open(file_from, "r") as json_file:
    data = json.load(json_file)  # Load data from the source file

# Call the function to write data to a new JSON file
write_json(data)
