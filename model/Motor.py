#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
# from sqlalchemy import Column, String, Boolean
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship



class Motor(BaseMachine,Base):
    """
    Represent a Motor.

    Attributes:
        name (str): The name of the Motor.
        code_model (str): The code_model of the Motor.
        Speed_max (str): The Speed_max of the Motor.
        Puissance (str): The Puissance of the Motor.
        detail (str): The detail of the Motor.
        img = ??
    """
    __tablename__ = 'motor'
    # id = Column(String(60), ForeignKey('machines.id'), primary_key=True)
    name = Column(String(128), nullable=False)
    code_model = Column(String(128), nullable=False)
    Speed_max = Column(String(128), nullable=False)
    Puissance = Column(String(128), nullable=False)
    detail = Column(String(128), nullable=False)
    reserved = Column(Boolean, default=False)
    # available_dates = Column(String(60), unique=False)  # Store available dates as a JSON string
    # __mapper_args__ = {
    #     'polymorphic_identity': 'motor',
    # }

    # machine = relationship("BaseMachine", back_populates="motors")
    reservation = relationship("Reservation", back_populates="motor")

    
    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)