#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine, Base


class Bike(BaseMachine):
    """
    Represent a Bike.

    Attributes:
        name (str): The name of the Bike.
        code_model (str): The code_model of the Bike.
        Speed_max (str): The Speed_max of the Bike.
        Puissance (str): The Puissance of the Bike.
        detail (str): The detail of the Bike.
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