#!/usr/bin/python3
"""
Defines the Admin class.
"""
from sqlalchemy import Column, ForeignKey, String
from model.Person import Person

class Admin(Person):
    """
    Represent a Admin.
    Attributes:

    """
    __tablename__ = 'admin'
    full_name = Column(String(60), nullable=False)
    id = Column(String(60), ForeignKey('person.id'), primary_key=True)
    email = Column(String(50), unique=True)
    image_path = Column(String(255), nullable=True)  # Store the file path of the uploaded image
    password = Column(String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
        'inherit_condition': (id == Person.id)
    }

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)
