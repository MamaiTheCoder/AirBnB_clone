#!/usr/bin/python3

"""Contain class BaseModel."""
import uuid
import model
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """class that defines all common attributes/methods for other classes."""
    def __init__(self, *args, **kwags):
        """Special method that initializes the base model."""
        if kwags:
            for key, value in kwags.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwags["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwags["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values."""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
