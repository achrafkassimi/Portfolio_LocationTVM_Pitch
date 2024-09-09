#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Customer(Base):
    """
    Represent a Customer.

    Attributes:

    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(60), nullable=False)
    # lname = Column(String(60), nullable=False)
    # Num_tel = Column(String(60), nullable=False)
    # CIN = Column(String(60), unique=True, nullable=False)
    # address = Column(String(128), nullable=False)
    # ville = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    # Relationship to Reservation
    reservation = relationship('Reservation', back_populates='customer')

    # def __init__(self, *args, **kwargs):
    #     """initializes User"""
    #     super().__init__(*args, **kwargs)    
