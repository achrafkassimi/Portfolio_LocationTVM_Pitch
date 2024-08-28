#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String


class Scooter(BaseMachine, Base):
    """
    Represent a Scooter.

    Attributes:
        name (str): The name of the Scooter.
        code_model (str): The code_model of the Scooter.
        Speed_max (str): The Speed_max of the Scooter.
        Puissance (str): The Puissance of the Scooter.
        detail (str): The detail of the Scooter.
        img = ??
    """
    __tablename__ = 'scooter'
    name = Column(String(128), nullable=False)
    code_model = Column(String(128), nullable=False)
    Speed_max = Column(String(128), nullable=False)
    Puissance = Column(String(128), nullable=False)
    detail = Column(String(256), nullable=False)
    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)