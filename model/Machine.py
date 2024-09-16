#!/usr/bin/python3
"""
Defines the Machine class.
"""
from model.BaseModel import BaseModel, Base
from sqlalchemy import Column, String


class Machine(BaseModel, Base):
    """
    Represent a Machine.
    Attributes:
    """
    __tablename__ = 'machine'
    model = Column(String(50), unique=True)
    type = Column(String(50))
    # Differentiates between Moto, Bike, Scooter
    
    __mapper_args__ = {
        'polymorphic_identity': 'machine',
        'polymorphic_on': type
    }
    

    def __init__(self, *args, **kwargs):
        """initializes Machine"""
        super().__init__(*args, **kwargs)