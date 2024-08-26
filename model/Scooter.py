#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine


class Scooter(BaseMachine):
    """
    Represent a Scooter.

    Attributes:
        name (str): The name of the Scooter.
        code_model (str): The code_model of the Scooter.
        Speed_max (str): The Speed_max of the Scooter.
        Puissance (str): The Puissance of the Scooter.
        detail (str): The detail of the Scooter.
        img = ??
    """

    name = ""
    code_model = ""
    Speed_max = ""
    Puissance = ""
    detail = ""
    # image = ??

    def __init__(self, *args, **kwargs):
        """initializes User"""
        super().__init__(*args, **kwargs)