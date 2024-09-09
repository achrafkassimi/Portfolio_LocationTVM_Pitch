#!/usr/bin/python3
"""
This module defines a base class for (T-V-M) models in our location_TVM clone
"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Boolean
import model
from sqlalchemy.orm import relationship
# from model.BaseMachine import Base



# from os import getenv

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()
#Base
class BaseMachine():
    """
        A base class for (T-V-M) models in our location_TVM clone
    """
    # __tablename__ = 'machines'
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    reserved = Column(Boolean, default=False)
    # __mapper_args__ = {
    #     'polymorphic_identity': 'machines'
    # }
    # Relationships to specific types of machines
    # bikes = relationship("Bike", back_populates="machine") # , uselist=False, cascade="all, delete-orphan"
    # motors = relationship("Motor", back_populates="machine")
    # scooters = relationship("Scooter", back_populates="machine")
    # reservation = relationship("Reservation", back_populates="machine")


    def __init__(self, *args, **kwargs):
        """
        Instantiates a new model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()


    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        # from model import storage
        self.updated_at = datetime.now()
        # print("test")
        model.storage.new(self)
        model.storage.save()

    def to_dict(self):
        """
        creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """
        delete function
        """
        from model import storage
        storage.delete(self)
