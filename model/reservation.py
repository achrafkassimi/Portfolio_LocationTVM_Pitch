#!/usr/bin/python3
"""
Defines the reservation class.
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

class reservation(Base):

    def __init__(self):     
        self.__id =None
        self.__nomber_jour =None
        self.__date_depart =None

    def Annuler (self):     
        # implementation
        pass        

    def Confirmed (self):       
        # implementation
        pass        

    
