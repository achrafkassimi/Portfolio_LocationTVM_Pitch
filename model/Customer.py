#!/usr/bin/python3
"""
Defines the Customer class.
"""
from model.Person import Person
from sqlalchemy import Column, ForeignKey, String

class Customer(Person):
    """
    Represent a Customer.
    Attributes:

    """
    __tablename__ = 'customer'
    id = Column(String(60), ForeignKey('person.id'), primary_key=True)
    email = Column(String(50), nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    num_tel = Column(String(60), nullable=False)
    cin = Column(String(60), nullable=False)
    address = Column(String(128), nullable=False)
    city = Column(String(60), nullable=False)
    gender = Column(String(60), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'inherit_condition': (id == Person.id)
    }

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
