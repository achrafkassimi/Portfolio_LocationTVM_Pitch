#!/usr/bin/python3
"""
Defines the User class.
"""
from model.BaseMachine import BaseMachine


class Motor(BaseMachine):
    """
    Represent a Motor.

    Attributes:
        name (str): The name of the Motor.
        code_model (str): The code_model of the Motor.
        Speed_max (str): The Speed_max of the Motor.
        Puissance (str): The Puissance of the Motor.
        detail (str): The detail of the Motor.
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