#!/usr/bin/python3
"""
Contains the FileStorage class.
"""
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'City': City, 'Amenity': Amenity, 'State': State,
        'Review': Review}


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    """string - path to the JSON file."""
    __file_path = "file.json"

    """dictionary - empty but will store all objects by <class name>.id."""
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file (__file_path) exists; 
        Otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised
        """
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
