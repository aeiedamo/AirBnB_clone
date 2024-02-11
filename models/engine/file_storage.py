#!/usr/bin/python3
"""this file constructs a FileStorage class"""
from json import dump, load
from models.base_model import BaseModel


class FileStorage:
    """
    this class serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """to return dictionary representation of an object"""
        return self.__objects

    def new(self, obj):
        """method to set in the obj with obj class id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes object attributes in json file as string"""
        to_save = {}
        with open(self.__file_path, "w+") as f:
            for obj in self.__objects.values():
                to_save[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()
            dump(to_save, f)

    def reload(self):
        """method that deserializes JSON to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                deserial = load(f)
                for obj in deserial.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
