#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
# from sqlalchemy import Column, String, Boolean
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship



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
    # id = Column(String(60), ForeignKey('machines.id'), primary_key=True)
    name = Column(String(128), nullable=False)
    code_model = Column(String(128), nullable=False)
    Speed_max = Column(String(128), nullable=False)
    Puissance = Column(String(128), nullable=False)
    detail = Column(String(256), nullable=False)
    reserved = Column(Boolean, default=False)
    # available_dates = Column(String(128), nullable=False)
    # __mapper_args__ = {
    #     'polymorphic_identity': 'scooter',
    # }

    # machine = relationship("BaseMachine", back_populates="scooters")
    reservation = relationship("Reservation", back_populates="scooter")

    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)