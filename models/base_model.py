#!/usr/bin/python3
"""This file is created to create a BaseModel class"""
from datetime import datetime
from uuid import uuid4
import unittest


class BaseModel:
    """this section defines a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """constructor for BaseModel objects"""
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """method to represent the class in a string"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """method to update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """method to return a dictionary representation of a class"""
        self.__dict__["created_at"] = (self.created_at).isoformat()
        self.__dict__["updated_at"] = (self.updated_at).isoformat()
        self.__dict__["__class__"] = type(self).__name__
        return self.__dict__


if __name__ == "__main__":
    unittest.TestCase()
