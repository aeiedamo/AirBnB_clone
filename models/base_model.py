#!/usr/bin/python3
"""This file defines a Base Model class"""
import uuid
import datetime
import models


class BaseModel:
    """This defines a BaseModel class"""

    def __init__(self, *args, **kwargs):
        """constructor for BaseModel class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """returns a string representation of an BaseModel object"""
        s = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return s

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates a diction representation of a BaseModel object"""
        obj_dict = (self.__dict__).copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
