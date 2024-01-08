#!/usr/bin/python3

# Import necessary modules
import uuid
from datetime import datetime
from basemodel import BaseModel  # Replace 'your_module' with the actual module containing the BaseModel class


# Import necessary modules
from user import User  # Replace 'models.user' with the actual path to the User class

# Create an instance of the User class
user_instance = User()

# Test the inherited __str__ method
print(str(user_instance))

# Test the inherited to_dict method
dict_representation = user_instance.to_dict()
print(dict_representation)

# Test the inherited save method
user_instance.save()
print(f"Updated at: {user_instance.updated_at}")

# Additional testing based on your specific methods and requirements
# ...


# Create an instance of the BaseModel class
base_model_instance = BaseModel()

# Test the __str__ method
print(str(base_model_instance))

# Test the to_dict method
dict_representation = base_model_instance.to_dict()
print(dict_representation)

# Test the save method
base_model_instance.save()
print(f"Updated at: {base_model_instance.updated_at}")

# Create another instance with a specific ID and test methods
custom_id_instance = BaseModel()
custom_id_instance.id = "custom_id"
print(str(custom_id_instance))


