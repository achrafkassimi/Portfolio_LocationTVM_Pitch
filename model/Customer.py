#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import column_property
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
        
    # def reserve_machine(self, machine, reserve_date):
    #     if reserve_date in self.reservations:
    #         print(f"{self.name} already has a reservation on {reserve_date}.")
    #         return False
    #
    #     if machine.reserve(reserve_date):
    #         self.reservations[reserve_date] = machine
    #         print(f"{self.name} successfully reserved Machine {machine.machine_id} on {reserve_date}.")
    #         return True
    #     else:
    #         print(f"Machine {machine.machine_id} is not available on {reserve_date}.")
    #         return False

    # def release_machine(self, release_date):
    #     if release_date in self.reservations:
    #         machine = self.reservations.pop(release_date)
    #         machine.release(release_date)
    #         print(f"{self.name} released Machine {machine.machine_id} on {release_date}.")
    #     else:
    #         print(f"{self.name} does not have any reservation on {release_date}.")

    # def __str__(self):
    #     reservations = ", ".join(f"{date}: Machine {machine.machine_id}" for date, machine in self.reservations.items())
    #     return f"Customer {self.name} reservations: {reservations if reservations else 'None'}"


