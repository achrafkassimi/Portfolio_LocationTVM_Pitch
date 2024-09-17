#!/usr/bin/python3
"""
Defines the Bike class.
"""
from model.Machine import Machine
from sqlalchemy import Column, ForeignKey, String, Boolean


class Bike(Machine):
    """
    Represent a Bike.

    Attributes:
        id (str): Unique identifier.
        name_bike (str): Name of the bike.
        image_path (str): Path to the image of the bike.
        engine (str): Details about the engine.
        batteries (str): Battery details.
        amperes (str): Amperage details.
        temps_charger (str): Charging time.
        speed_max (str): Maximum speed.
        autonomic (str): Range of the bike.
        detail (str): Additional details.
        reserved (bool): Reservation status.

    """
    __tablename__ = 'bike'
    id = Column(String(60), ForeignKey('machine.id'), primary_key=True)
    name_bike = Column(String(128), nullable=False)
    image_path = Column(String(255), nullable=True)  # Store the file path of the uploaded image
    engine = Column(String(128), nullable=False) # Moteur 500W nominal
    batteries = Column(String(128), nullable=False)
    amperes = Column(String(128), nullable=False)
    temps_charger = Column(String(128), nullable=False)
    speed_max = Column(String(128), nullable=False) # Possibilité de jusqu'à 40km/h (selon le poids, l'itinéraire et la charge de la batterie)
    autonomic = Column(String(128), nullable=False) # Possibilité jusqu'à 50km Maximum (en fonction du poids, de l'itinéraire et de la charge de la batterie)

    detail = Column(String(256), nullable=False)
    reserved = Column(Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'bike',
        'inherit_condition': (id == Machine.id)
    }

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)