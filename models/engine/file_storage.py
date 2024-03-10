#!/usr/bin/python3
"""File Storage Module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DataStorage:
    """Abstracted storage engine for handling data serialization and deserialization."""

    FILE_PATH = "data_storage.json"
    OBJECTS = {}

    def get_all(self):
        """Retrieve all stored objects."""
        return DataStorage.OBJECTS

    def add_new(self, obj):
        """Add a new object to the storage."""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        DataStorage.OBJECTS[key] = obj

    def save_data(self):
        """Serialize objects and save to a JSON file."""
        objects_dict = {key: obj.to_dict() for key, obj in DataStorage.OBJECTS.items()}
        with open(DataStorage.FILE_PATH, "w") as file:
            json.dump(objects_dict, file)

    def load_data(self):
        """Deserialize the JSON file to retrieve stored objects."""
        try:
            with open(DataStorage.FILE_PATH) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.add_new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
