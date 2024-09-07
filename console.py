#!/usr/bin/python3
"""
Module for console
"""
import cmd
import shlex
import re
import ast
import model
from model.__init__ import storage
from model.BaseMachine import BaseMachine
from model.Scooter import Scooter
from model.Motor import Motor
from model.Bike import Bike
from sqlalchemy.orm import sessionmaker

class LocationTVM_Command(cmd.Cmd):
    """
    Attributes LocationTVM_Command console class
    prompt 
    classes
    """
    prompt = "(Location_TVM) "
    valid_classes = ["BaseMachine", "Scooter", "Motor", "Bike", "CalendarDate", "Reservation", "Customer"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass
    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program
        """
        print('Exiting...')
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        print('Exiting...')
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
            # print(commands[1])
            # key = "{}.{}".format(commands[0], commands[1])
            # print(key) # Bike.78013a16-bf8a-4cd3-96ad-b410003ce651
            for k in objects.keys():
                if commands[1] in k and commands[0] in k:
                    v = objects[k]

            storage.delete(v)
            storage.save()

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: all <name_class> # for instances in class specific
            or all              # for instances in all class
        """
        objects = storage.all()
        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in objects.items():
                # print(str(value)) # print all instances classes
                print('{} : {}'.format(key, value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print('{} : {}'.format(key, value))

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: count <class name>   # for instances in class specific
            or count                # for instances in all class
        """
        objects = storage.all()
        commands = shlex.split(arg)
        count = 0
        # print(commands)

        if len(commands) == 0:
            for key, _ in objects.items():
                count += 1
            print("for all class count = ",count)
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, _ in objects.items():
                if key.split('.')[0] == commands[0]:
                    count += 1
            print("for class {} count = {}".format(commands[0], count))

    def do_all_class(self, arg):
        """
        Print the string representation of all class exist .
        """
        for x in self.valid_classes:
            print(x)
        return True

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        example update Bike 91efd02a-472f-4f15-a5be-f4a9533dafd3 created_at "2024-08-29 01:06:53" updated_at "2024-08-29 01:06:53" name "44test"  code_model "i125" Speed_max "789" Puissance "266" detail "test teat"
        """
        commands = shlex.split(arg)
        # print(commands,"/n")

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            # print(objects)
            # print(commands[0], commands[1])
            key = "{}.{}".format(commands[0], commands[1])
            # oobjc = storage.get(commands[0], commands[1])
            # print(oobjc)
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                # print(obj, type(obj))
                curly_braces = re.search(r"\{(.*?)\}", arg)
                # print(curly_braces)

                if curly_braces:
                    # added to catch errors
                    print("# added to catch errors curly_braces")
                    try:
                        str_data = curly_braces.group(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        # added to catch exception
                        # try:
                            # attr_name1 = attribute_names[0]
                            # attr_value1 = attribute_values[0]
                            # setattr(obj, attr_name1, attr_value1)
                        # except Exception:
                        #     pass
                        # try:
                            # added to catch exception
                            # attr_name2 = attribute_names[1]
                            # attr_value2 = attribute_values[1]
                            # setattr(obj, attr_name2, attr_value2)
                            # obj.attr_name2 = attr_value2
                        # except Exception:
                        #     pass
                    except Exception:
                        pass
                else:

                    # attr_name = commands[2]
                    # attr_value = commands[3]
                    # print(attr_name)
                    # print(attr_value)
                    
                    # try:
                    #     attr_value = eval(attr_value)
                    # except Exception:
                    #     pass

                    kkey = []
                    vvalues = []

                    for i, x in enumerate(commands, 1):
                        if i % 2 == 0:    # check to see if it hit the interval threshold?
                            vvalues.append(x)
                        else:
                            kkey.append(x)
                    
                    # print(kkey)
                    # print(vvalues)

                    kkey.pop(0)
                    vvalues.pop(0)

                    for u, o in zip(kkey,vvalues):
                        # print(u, o)
                        setattr(model.storage.all()[key], u, o)

                    # setattr(model.storage.all()[key], attr_name, attr_value)
                    ## obj.name = attr_value
                    ## print(obj, type(obj))
                    ## obj.save() # ???????????????
                    ## print(model.storage.all()[key])
                ## storage.save()
                model.storage.all()[key].save()





if __name__ == "__main__":
    LocationTVM_Command().cmdloop()