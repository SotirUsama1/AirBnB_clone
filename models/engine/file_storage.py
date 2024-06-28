#!/usr/bin/python3
"""
File Storage
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    The Storage engine
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        """
        Returns all objects in dict __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds new object to the dict __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves objects in __objects dict in the json file
        """
        objs_dict = {}

        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(objs_dict, f)

    def reload(self):
        """
        Reads then converts objects from the json file to __objects dict
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_objs_dict = json.load(f)
            for key, obj in new_objs_dict.items():
                self.__objects[key] = self.class_dict[obj['__class__']](**obj)
        except FileNotFoundError:
            pass
