#!/usr/bin/python3
"""
Defines the reservation class.
"""
from model.BaseMachine import BaseMachine, Base
from sqlalchemy import Column, String
from model import Bike
# from CalendarDate import CalendarDate
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


class Reservation(Base):
    __tablename__ = 'reservation'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    # bike_id = Column(String(60), ForeignKey('bike.id'), nullable=False)
    # motor_id = Column(String(60), ForeignKey('motor.id'), nullable=False)
    # scooter_id = Column(String(60), ForeignKey('scooter.id'), nullable=False)
    machine_id = Column(String(60), ForeignKey('machines.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    customer = relationship("Customer", back_populates="reservation")
    machines = relationship("BaseMachine", back_populates="reservation")
    # Relationships
    # customer = relationship('Customer', backref='reservation', cascade="all, delete, delete-orphan")
    # bike = relationship('Bike', backref='reservation', cascade="all, delete, delete-orphan")
    # motor = relationship('Motor', backref='reservation', cascade="all, delete, delete-orphan")
    # scooter = relationship('Scooter', backref='reservation', cascade="all, delete, delete-orphan")
    
    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs) 

    # def add_machine(self, machine):
    #     self.machines[machine.machine_id] = machine

    # def add_customer(self, customer):
    #     self.customers[customer.name] = customer

    # def reserve_machine(self, customer_name, machine_id, year, month, day):
    #     customer = self.customers.get(customer_name)
    #     machine = self.machines.get(machine_id)
    #     reserve_date = CalendarDate(year, month, day)

    #     if not customer:
    #         print(f"Customer {customer_name} not found.")
    #         return False

    #     if not machine:
    #         print(f"Machine {machine_id} not found.")
    #         return False

    #     return customer.reserve_machine(machine, reserve_date)

    # def release_machine(self, customer_name, year, month, day):
    #     customer = self.customers.get(customer_name)
    #     release_date = CalendarDate(year, month, day)

    #     if not customer:
    #         print(f"Customer {customer_name} not found.")
    #         return False

    #     customer.release_machine(release_date)
    #     return True

    # def __str__(self):
    #     machines_status = "\n".join(str(machine) for machine in self.machines.values())
    #     return f"Reservation System Status:\n{machines_status}"
     

    
