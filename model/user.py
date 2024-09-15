#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(UserMixin, BaseMachine, Base):
    """
    Represent a User.

    Attributes:

    """
    __tablename__ = 'user'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(60), nullable=False)
    # lname = Column(String(60), nullable=False)
    # Num_tel = Column(String(60), nullable=False)
    # CIN = Column(String(60), unique=True, nullable=False)
    # address = Column(String(128), nullable=False)
    # ville = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    # Relationship to Reservation
    reservation = relationship('Reservation', back_populates='user')

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
