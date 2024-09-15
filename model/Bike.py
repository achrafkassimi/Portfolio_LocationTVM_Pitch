#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
# from sqlalchemy import Column, String, Boolean
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship



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
    # id = Column(String(60), ForeignKey('machines.id'), primary_key=True)
    name = Column(String(128), nullable=False)
    code_model = Column(String(128), nullable=False)
    Speed_max = Column(String(128), nullable=False)
    Puissance = Column(String(128), nullable=False)
    detail = Column(String(128), nullable=False)
    reserved = Column(Boolean, default=False)
    # available_dates = Column(Boolean, unique=False)
    # __mapper_args__ = {
    #     'polymorphic_identity': 'bike',
    # }

    # machine = relationship("BaseMachine", back_populates="bikes")
    reservation = relationship("Reservation", back_populates="bike")

    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)