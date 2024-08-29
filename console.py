#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
import re
import ast
from model.__init__ import storage
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

    def do_how(self, line): # , line for print sum line
        """
        function help
        just help name function "help create" ==> comment in ths function
        """
        print("quit command to exit the program")
        print("EOF (Ctrl+D) signal to exit the program")
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
        # print("")
    
    def do_create(self, arg):
        """
        Create a new instance and save it to the DB data mysql
        Usage:      create <class_name> parameter1=".." parameter2=".." ...
        example:    create Bike name="" code_model="" Speed_max="" Puissance="" detail=""
        """
        try:
            class_name = arg.split(" ")[0]
            # print(class_name)
            if len(class_name) == 0:
                print("** class name missing **")
                return
            if class_name and class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            kwargs = {}
            commands = arg.split(" ")
            for i in range(1, len(commands)):
                key = commands[i].split("=")[0]
                value = commands[i].split("=")[1]
                # key, value = tuple(commands[i].split("="))
                if value.startswith('"'):
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
            # print(kwargs)
            
            if kwargs == {}:
                new_instance = eval(class_name)()
            else:
                new_instance = eval(class_name)(**kwargs)
            storage.new(new_instance)
            # print(new_instance.id)
            storage.save()
            
        except ValueError:
            print(ValueError)
            return

    def do_show(self, arg):
        """
        Show the object representation of model instance by id.
        Usage: show <class_name> <id>
        example: show Bike d52a014c-7652-49e2-bf49-b587bb79f5d7
        """
        commands = shlex.split(arg)
        # print(commands)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            # print(objects)
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                # print(objects[key])
                obj_vars = vars(objects[key])
                for k, v in obj_vars.items():
                    # print(k, v)
                    print('{} : {}'.format(k, v))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        example: destroy Bike 78013a16-bf8a-4cd3-96ad-b410003ce651
        """
        commands = shlex.split(arg)
        # print(commands) # ['Bike', '78013a16-bf8a-4cd3-96ad-b410003ce651']
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            # print(objects) # {'Scooter.dada58ca-fd6b-4ca9-af01-519fe7248fc8': <model.Scooter.Scooter object at 0x000002C3D2034830>, 'Motor.462106f8-4fce-46c9-bb7e-68e65d8adc53': <model.Motor.Motor object at 0x000002C3D2035700>, 'Bike.78013a16-bf8a-4cd3-96ad-b410003ce651': <model.Bike.Bike object at 0x000002C3D2036780>, 'Bike.91efd02a-472f-4f15-a5be-f4a9533dafd3': <model.Bike.Bike object at 0x000002C3D2036720>, 'Bike.d52a014c-7652-49e2-bf49-b587bb79f5d7': <model.Bike.Bike object at 0x000002C3D20366C0>}
            key = "{}.{}".format(commands[0], commands[1])
            # print(key) # Bike.78013a16-bf8a-4cd3-96ad-b410003ce651
            if key in objects:
                del objects[key]
                # storage.delete(key)
                # storage.all().pop(key)
                storage.save()
                # storage.reload()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        pass

    def do_count(self, arg):
        """
        """
        pass

    def do_all_class(self, arg):
        """
        Print the string representation of all class.
        """
        pass

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        """
        pass




if __name__ == "__main__":
    LocationTVM_Command().cmdloop()