#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String



    # __tablename__ = 'bike'
    # name = Column(String(128), nullable=False)
    # code_model = Column(String(128), nullable=False)
    # Speed_max = Column(String(128), nullable=False)
    # Puissance = Column(String(128), nullable=False)
    # detail = Column(String(128), nullable=False)
    # # image = ??

    # def __init__(self, *args, **kwargs):
    #     """initializes User"""
    #     super().__init__(*args, **kwargs)


class Client:
    """
    Represent a Bike.

    Attributes:

    """
    def __init__(self):     

        self.__id =None
        self.__nom =None
        self.__prenom =None
        self.__tele =None
        self.__CIN =None
        self.__email =None