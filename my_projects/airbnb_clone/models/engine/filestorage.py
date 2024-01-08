#!/usr/bin/python3

"""File Storage class
for serialization into a JSON file and
deserialization of JSON file
into an instances.
"""

import json
from os import path
from models.user import User
from models.basemodel import BaseModel

class FileStorage:

    """
        Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
    }

    __file_path = "file.json"  # path to the JSON file

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file does not exist, no exception should be raised.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of
                    # the class based on class_name
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance


"""
Loop Through Instances:

for key, obj in self.__objects.items():: Iterates through the dictionary __objects, where keys are instance keys (usually a combination of class name and instance ID), and values are instances themselves.
Serialize Instances:

serialized_objects[key] = obj.to_dict(): Calls the to_dict method on each instance (obj) to obtain a dictionary representation of the instance. This dictionary is then added to serialized_objects, with the instance key as the key in serialized_objects.
Open JSON File:

with open(self.__file_path, 'w') as file:: Opens the JSON file specified by __file_path in write mode.
Write Serialized Data to File:

json.dump(serialized_objects, file): Writes the serialized data (in the form of a dictionary) to the opened file using the json.dump function.
In summary, the save method iterates through instances stored in __objects, converts each instance to a dictionary using the to_dict method, and then writes the serialized instances to a JSON file specified by __file_path. This ensures that the state of the instances is persisted in a JSON file, allowing for later retrieval and reconstruction of instances."""

""""""


"""
def reload(self):
    
    Deserializes the JSON file to __objects.
    Only if the JSON file (__file_path) exists; otherwise, do nothing.
    If the file does not exist, no exception should be raised.
    
    if path.exists(self.__file_path):
        with open(self.__file_path, 'r') as file:
            serialized_objects = json.load(file)
            for key, obj_data in serialized_objects.items():
                class_name, obj_id = key.split('.')
                # Dynamically create an instance of
                # the class based on class_name
                obj_class = globals()[class_name]
                obj_instance = obj_class(**obj_data)
                # Store the instance in __objects
                self.__objects[key] = obj_instance
"""