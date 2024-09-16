#!/usr/bin/python3
"""
Defines the Motor class.
"""
from model.Machine import Machine
from sqlalchemy import Column, ForeignKey, String, Boolean



class Motor(Machine):
    """
    Represent a Motor.

    Attributes:

    """
    __tablename__ = 'motor'
    id = Column(String(60), ForeignKey('machine.id'), primary_key=True)
    name_motor = Column(String(128), nullable=False)
    image_path = Column(String(255), nullable=True)  # Store the file path of the uploaded image
    maximal_moto = Column(String(128), nullable=False)
    batteries  = Column(String(128), nullable=False)
    speed_max = Column(String(128), nullable=False)
    autonomic = Column(String(128), nullable=False)
    charger = Column(String(128), nullable=False)
    temps_charger =  Column(String(128), nullable=False)
    charge_max = Column(String(128), nullable=False)

    detail = Column(String(128), nullable=False)
    reserved = Column(Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'motor',
        'inherit_condition': (id == Machine.id)
    }

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)