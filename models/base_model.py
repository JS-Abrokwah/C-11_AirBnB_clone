#!/usr/bin/python3
""" AirBnB BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Definition of the BaseModel """

    def __init__(self):
        """ Initializes a new instance of BaseModel
        """
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """ updates the instance attribute update_at with current datetime"""
        self.update_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Includes the key/value pair __class__ representing the class name
        of the object."""
        instance_dict = self.__dict__.copy()
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict

    def __str__(self):
        """ String representation of BaseModel instances"""
        return "[<{}>] (<{}>) <{}>".format(self.__class__.__name__,
                                          self.id, self.__dict__)
