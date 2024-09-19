#!/usr/bin/python3
"""
Defines the Person class.
"""
from sqlalchemy import Column, String
from model.BaseModel import BaseModel, Base

# Base class for all persons
class Person(BaseModel, Base):
    """
    Represent a Person.
    Attributes:

    """
    __tablename__ = 'person'
    username = Column(String(50), unique=True)
    type = Column(String(50))
    
    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }