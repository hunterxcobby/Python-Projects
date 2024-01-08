#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class for creating and managing instances.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        # Create a copy of the instance's attributes dictionary
        obj_dict = self.__dict__.copy()

        # Add a key '__class__' with the value being the name of the class
        obj_dict['__class__'] = self.__class__.__name__

        # Convert 'created_at' timestamp to ISO format and add to the dictionary
        obj_dict['created_at'] = self.created_at.isoformat()

    def __str__(self):
        """Return a string representation of the instance."""
        # Get the class name of the instance
        class_name = self.__class__.__name__

        # Return a formatted string with class name, id, and instance attributes
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)



"""
Converting the `created_at` and `updated_at` timestamps to ISO format before including them in the dictionary provides several benefits:

1. **Standardized Format:**
   - ISO 8601 format (e.g., "2022-01-15T12:30:45.678900") is a widely recognized and standardized representation of date and time.
   - It ensures consistency in how timestamps are stored and communicated.

2. **Readability:**
   - ISO format is human-readable and follows a clear structure, making it easy for developers and users to understand the timestamp.

3. **Compatibility:**
   - ISO format is compatible with various systems, databases, and serialization formats.
   - It simplifies interoperability when exchanging data between different applications or services.

4. **Sorting and Comparison:**
   - ISO-formatted timestamps are sortable and comparable as strings. This is useful when sorting data chronologically or when comparing timestamps.

5. **Serialization:**
   - ISO format is commonly used when serializing data, especially in formats like JSON. Many libraries and APIs expect timestamps in ISO format for consistency.

6. **Database Integration:**
   - When storing data in databases, using ISO-formatted timestamps ensures compatibility with database systems that support date and time types.

Here's an example of how the ISO format looks:
```plaintext
2022-01-15T12:30:45.678900
```

In summary, converting timestamps to ISO format is a best practice for standardization, readability, compatibility, and ease of use in various contexts, especially when dealing with data storage, exchange, and serialization."""


"""
Human-Readable Output:

The string representation is designed to be easily readable by humans. It provides a concise yet informative summary of the instance's attributes.
This is particularly useful for debugging and logging, where developers can quickly inspect the state of an object.
Printable Output:

When an object is printed using the print function or included in formatted strings, the __str__ method determines what gets displayed.
It allows developers to obtain meaningful information about the instance without needing to inspect its attributes individually.

Consistency with Built-In Functions:

When using built-in functions like str or print, the __str__ method is automatically called if available. This ensures consistency in how instances are represented as strings across different parts of your code."""


