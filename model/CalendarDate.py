#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from datetime import date

class CalendarDate(Base):
    __tablename__ = 'calendar_dates'
    
    id = Column(String(60), primary_key=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)


    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
