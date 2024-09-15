#!/usr/bin/python3
"""
Defines the reservation class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Reservation(BaseMachine, Base):

    __tablename__ = 'reservation'

    # id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(String(60), ForeignKey('customer.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    bike_id = Column(String(60), ForeignKey('bike.id'), nullable=True)
    motor_id = Column(String(60), ForeignKey('motor.id'), nullable=True)
    scooter_id = Column(String(60), ForeignKey('scooter.id'), nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    prix = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="reservation")
    user = relationship("User", back_populates="reservation")
    # machine = relationship("BaseMachine", back_populates="reservation")
    bike = relationship('Bike', back_populates='reservation')
    motor = relationship('Motor', back_populates='reservation')
    scooter = relationship('Scooter', back_populates='reservation')


    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs) 
