#!/usr/bin/python3
"""this file create a FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """create a FileStorage class"""

    def __init__(self) -> None:
        """constructor for FileStorage object"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """method ro return the objects loaded"""
        return self.__objects

    def new(self, obj):
        """method to set in __objects the obj with key obj.id"""
        objkey = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[objkey] = obj

    def save(self):
        """method to serialize to JSON file"""
        with open(self.__file_path, "w") as f:
            to_dump = {}
            for key, value in self.__objects.items():
                to_dump[key] = value.to_dict()
            json.dump(to_dump, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Review": Review,
        }
        with open(self.__file_path, "r") as f:
            to_load = json.load(f)
            self.__objects = {
                k: classes[k.split(".")[0]](**v) for k, v in to_load.items()
            }
