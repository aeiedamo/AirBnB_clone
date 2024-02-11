#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """constructs a new BaseModel object"""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.datetime.fromisoformat(v)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Represents object as dictionary"""
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        """Represents class as a string"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
