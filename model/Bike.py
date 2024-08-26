#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String


class Bike(BaseMachine, Base):
    """
    Represent a Bike.

    Attributes:
        name (str): The name of the Bike.
        code_model (str): The code_model of the Bike.
        Speed_max (str): The Speed_max of the Bike.
        Puissance (str): The Puissance of the Bike.
        detail (str): The detail of the Bike.
        img = ??
    """
    __tablename__ = 'bike'
    name = Column(String(128), nullable=False)
    code_model = Column(String(128), nullable=False)
    Speed_max = Column(String(128), nullable=False)
    Puissance = Column(String(128), nullable=False)
    detail = Column(String(128), nullable=False)
    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)