#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
import re
import ast
from model.BaseMachine import BaseMachine
from model.Scooter import Scooter
from model.Motor import Motor
from model.Bike import Bike


class LocationTVM_Command(cmd.Cmd):
    """
    Attributes LocationTVM_Command console class
    """
    prompt = "(Location_TVM) "
    valid_classes = ["BaseMachine", "Scooter", "Motor", "Bike"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def help_quit(self):
        """
        """
        print("Quit command to exit the program")
        print("")   