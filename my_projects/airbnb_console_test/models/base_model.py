#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for creating and managing instances.
    """
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

        Args:
            - *args: arguments
            - **kwargs: a dictionary of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, self.TIME_FORMAT)
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self) -> None:
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Returns a dictionary of all keys/values of __dict__ of the instance.
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__

        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()

        return result
