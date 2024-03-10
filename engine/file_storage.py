#!/usr/bin/python3
"""FileStorage class for managing object serialization."""
import json
from ..models.base_model import BaseModel
from ..models.user import User
from ..models.state import State
from ..models.city import City
from ..models.place import Place
from ..models.amenity import Amenity
from ..models.review import Review
class FileStorage:
    """A class to manage object serialization."""
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Return a dictionary of all objects."""
        return self.__objects
    def new(self, obj):
        """Add a new object to the object dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """Serialize objects to a JSON file."""
        serialized_objs = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objs, file)
    def reload(self):
        """Deserialize the JSON file."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
                      return
