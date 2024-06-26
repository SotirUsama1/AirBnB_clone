#!/usr/bin/python3
"""
This the base model for the classes in this project
"""

from datetime import datetime
from uuid import uuid4

class BaseModel():
    """Base Model class which all the other classes inherit from
    """

    def __init__(self):
        """
        Initializes attributes: uuid4, dates when class was created/updated
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        prints the passed object in a string standarized form
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Saves the update on the called object
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
