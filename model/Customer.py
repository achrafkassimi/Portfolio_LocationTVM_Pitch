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
    image_path = Column(String(255), nullable=True)  # Store the file path of the uploaded image

    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    Num_tel = Column(String(60), nullable=False)
    CIN = Column(String(60), unique=True, nullable=False)
    address = Column(String(128), nullable=False)
    ville = Column(String(60), nullable=False)
    password = Column(String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'inherit_condition': (id == Person.id)
    }

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
