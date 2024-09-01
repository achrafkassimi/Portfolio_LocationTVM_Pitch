#!/usr/bin/python3
"""
Defines the reservation class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String


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

    
