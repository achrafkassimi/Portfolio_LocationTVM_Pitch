#!/usr/bin/python3
"""
Defines the reservation class.
"""
from datetime import datetime
from model.BaseModel import BaseModel, Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Reservation(BaseModel, Base):

    __tablename__ = 'reservation'
    person_id = Column(String(60), ForeignKey('person.id'), nullable=False)
    machine_id = Column(String(60), ForeignKey('machine.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    prix = Column(Integer, nullable=False)

    # Relationships to Person and Machine
    person = relationship("Person")
    machine = relationship("Machine")

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs) 
